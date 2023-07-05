
from dfs_findArb import*
from web3.auto import Web3
import asyncio
import json
import time
from dfs_findArb import*
from commonn import*
from router import*
from thread import *
from decimal import Decimal
import requests
# from call_contract import*
from lookevents import*
from rpc import*
# pairs = 

http = 'http://176.9.26.145:8545'#https://mmf-rpc.xstaking.sg
web3 = Web3(Web3.HTTPProvider(http))

# print(web3.isConnected())
tokenIn ={
            'address': '0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23',
            'symbol': 'WCRO',
            'decimal': 18,
            }
            
tokenOut = tokenIn
maxHops = 3
amountIn = 50*pow(10,18)
gasPrice = 5000
currentPairs = []
path = [tokenIn]
bestTrades = []

router_list = [ 



]
pairsnew = []
def handle_event(event):
    pairs_all = json.load(open('pairs_dexscreener.json'))
    pairs = pairs_all
    #print(Web3.toJSON(event))
    try:
        getTrans = Web3.toJSON(event).strip('"')
        # print(web3.eth.get_transaction(getTrans))
        trans = web3.eth.get_transaction(getTrans)
        print(trans)
        print('--------------------------------------')
        data = trans['input']
        to = trans['to']

        if to == MMF_ROUTER_ADDRESS:
            decoded = MMF_ROUTER_CONTRACT.decode_function_input(data)
            #print(decoded, 'time:', time.time())
        elif to == VVS_ROUTER_ADDRESS:
            decoded = VVS_ROUTER_CONTRACT.decode_function_input(data)
            #print(decoded, 'time:', time.time())
        elif to == CRONA_ROUTER_ADDRESS:
            decoded = CRONA_ROUTER_CONTRACT.decode_function_input(data)
            #print(decoded, 'time:', time.time())

        
        #path_add = decoded[1]['path']
            # path_add.reverse()
            # tokenOut1 = path_add[0]
            # tokenIn1 = path_add[-1]
            # print(tokenIn1, tokenOut1)
            # pairs =get_reserves(pairs)
            # besttrade1 = findArb(pairs, tokenIn, tokenOut1, maxHops, currentPairs, path, bestTrades)
            # path2 = [tokenIn1]
            # besttrade2 = findArb(pairs, tokenIn1, tokenIn, maxHops, currentPairs, path2, bestTrades)
            
            # print(besttrade1)
            # print('--------------------')
            # print(besttrade2)
            # s = time.time()
            
            # trades = findArb(pairs, tokenIn, tokenOut, maxHops, currentPairs, path, bestTrades)
            # # print(trades[0])
            # trade = trades[0]
            # print('PROFIT:', trade['p'])
            # print('TIME GET RES AND FIND ARB:', time.time() - s)


        else:
            print('nothing')
        #print('method:',decoded[0])
        
    except Exception as e:
        print(f'error occurred: {e}')



async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
   # block_filter = w3.eth.filter('latest')
    tx_filter = web3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                #log_loop(block_filter, 2),
                log_loop(tx_filter, 1)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()
