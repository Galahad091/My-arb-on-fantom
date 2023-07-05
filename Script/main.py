
# import the following dependencies
import json
from web3 import Web3
# import asyncio
from dfs import*
from common import*
from router import*
from thread import *
from decimal import Decimal
import requests
import time 
from events import*
from rpc import*
# add blockchain connection information 
cronos_mainnet_rpc = "https://fantom-mainnet.gateway.pokt.network/v1/lb/6261a8a154c745003bcdb0f8" # 'http://34.125.72.89:8545'
w3 = Web3(Web3.HTTPProvider(cronos_mainnet_rpc, request_kwargs={'timeout': 6000}))  #websocket_timeout= 6000
ERC20ABI = json.load(open('./erc20.abi'))
IUniswapRouter_abi = json.load(open('./IUniswapV2Router.json'))
#smart contract
# wallet_addr = "0x60Eac9D8C91Fb1ee58014D3765AF84035d1F0338"
# privkey = "22ffdd314c2e798f2f292a2a56666fa36eb9b649c14a259f41446f8159e05c12" 
# mycontract_addr = Web3.toChecksumAddress("0xa40247665AC78a64de399b5E2eCd9CD3284866b6") 
# contract_abi = json.load(open('contract/contract_abi.json'))
# mycontract = w3.eth.contract(address = mycontract_addr, abi= contract_abi)

tokenIn ={
            'address': '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83',
            'symbol': 'WFTM',
            'decimal': 18,
            }
            
tokenOut = tokenIn
maxHops = 4
# amountIn = 50*pow(10,18)
gasPrice = 5000
currentPairs = []
path = [tokenIn]
bestTrades = []
pairs_all = json.load(open('pairs_dexscreener_copy1.json'))

# def MultiSwap(trade, pairs_addr, amount0Out, amount1Out, tradeoptimalAmount):
    # router_path = [router['router:'] for router in trade['route']]
    # path = [p['address'] for p in trade['path']]
    # print('router_path:',router_path)
    # print('path:',path)

    # tx = mycontract.functions.multiswap_Vm(pairs_addr, amount0Out, amount1Out, tradeoptimalAmount ).buildTransaction({
    #     'from': wallet_addr,
    #     'value': 0,
    #     'gasPrice': gasPrice,
    #     'gas': 800000,
    #     "nonce": w3.eth.getTransactionCount(wallet_addr),
    #     })
    # try:
    #     gasEstimate = w3.eth.estimateGas(tx)
    #     print('gasEstimate:',gasEstimate)
    #     fee = gasEstimate*gasPrice/pow(10,9)
    #     print('estimate fee:', fee)
    # except Exception as e:
    #     print('gas estimate err:', e)
    #     return None
    # if  fee < trade['p']:
    #     signed_tx = w3.eth.account.sign_transaction(tx, private_key=privkey)
    #     try:
    #         txhash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    #         return txhash.hex()
    #         print('DONE TRADE!!!')
    #     except:
    #         print('Trade False!!!')
    # else:
    #     print('Fee too much!!!')
    # print('-----------------------------------------------')


#GET AMOUNTOUT BY PATH: tính amountout từng pair và xếp vào list amount0Out, amount1Out tương ứng để truyền vào smartcontract
def getAmountsOut(trade, tradeoptimalAmount): 
    route = trade['route']
    router_list = [router['router:'] for router in route]
    path = [p['address'] for p in trade['path']]
    amount0Out = []
    amount1Out = []
    for i in range(len(router_list)):
        path_pair = []
        address = Web3.toChecksumAddress(router_list[i])
        UniRouter = w3.eth.contract(address=address, abi=IUniswapRouter_abi)
        if i == 0:
            amount = tradeoptimalAmount  
            # path_pair.extend(path[i:i+2])
            # amountsOut_list = UniRouter.functions.getAmountsOut(amount, path_pair).call()
            # if path[i] == route[i]['token0']['address']:
            #     amount0Out.append(0)
            #     amount1Out.append(amountsOut_list[-1])
            # elif path[i] == route[i]['token1']['address']:
            #     amount1Out.append(0)
            #     amount0Out.append(amountsOut_list[-1])

        elif i > 0 :
            amount = amountsOut_list[-1]

        path_pair.extend(path[i:i+2])
        amountsOut_list = UniRouter.functions.getAmountsOut(amount, path_pair).call()
        if path[i] == route[i]['token0']['address']:
            amount0Out.append(0)
            amount1Out.append(amountsOut_list[-1])
        elif path[i] == route[i]['token1']['address']:
            amount1Out.append(0)
            amount0Out.append(amountsOut_list[-1])
                
    return amount0Out, amount1Out

def main():
    global pairs, pairsDict, needChangeKey, w3, cronos_mainnet_rpc, mycontract, address
    pairs = randSelect(pairs_all)
    # pairsDict = toDict(pairs) #Sync block
    start = time.time()
    # pairs = threadpair(pairs) use when len(pairs) >200
    pairs =get_reserves(pairs)
    # print(pairs)
    restime = time.time()
    # print('Time to get reserves:', restime - start, 's')
    trades = findArb(pairs, tokenIn, tokenOut, maxHops, currentPairs, path, bestTrades)
    # print(trades)
    if len(trades)> 0:
        print('TRADE 1 PROFITTTTTTTTTTTTTTTTTTTTTTTTTTTTT:', trades[0]['p'])  
        end = time.time()
        # print('Tine to find arb:', end - restime, 's')
        # print('TOTAL TIMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE:', time.time() - start)
        trade = trades[0]
        pairs_addr = [pair['address'] for pair in trade['route']]
        # print(trade)
        tradeoptimalAmount = int(trades[0]['optimalAmount'])
        print('optimallllll:', (tradeoptimalAmount/pow(10,18)))
    else:
        print("No trade")
    # balance = mycontract.functions.getBalance(tokenIn['address']).call()
    # if not tradeoptimalAmount < balance:
    #     tradeoptimalAmount = balance  

    # amount0Out, amount1Out = getAmountsOut(trade, tradeoptimalAmount)
    # print('GetamountsOut TIME:', time.time() - end)
    # print('pairs_addr:',pairs_addr)
    # print('amount0Out:', amount0Out)
    # print('amount1Out:', amount1Out)
    # print('tradeoptimalAmount:', tradeoptimalAmount)
    # MultiSwap(trade, pairs_addr, amount0Out, amount1Out, tradeoptimalAmount)
    # print('TO TOTAL TIMEEEEE:', time.time() - start)
    # print('-------------------------------------------------------')

if __name__ == "__main__":
    # main()
    while 1:
        try:
            main()
        except Exception as e:
            print('exception:', e)
            raise

