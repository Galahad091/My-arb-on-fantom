import json
from web3 import Web3
from decimal import Decimal
from router import*
import time
# add blockchain connection information

cronos_mainnet_rpc = "ws://rpc.vvs.finance/"
w3 = Web3(Web3.WebsocketProvider(cronos_mainnet_rpc, websocket_timeout= 6000))
ERC20ABI = json.load(open('./erc20_abi.abi'))

#getSelector("swapExactTokensForTokens(uint256,uint256,address[],address,uint256)")= 0x38ed1739
#getSelector("swapExactETHForTokens(uint256 amountOutMin, address[] path, address to, uint256 deadline)")= 0x7ff36ab5
#getSelector("swapExactTokensForETH(uint256,uint256,address[],address,uint256)")= 0x18cbafe5

mycontract = '0x109C48345e84459C658e79e806F6DdB236DbDD26'
# multilswap = Web3.toChecksumAddress(mycontract)
# multilswap_abi = json.loads()
# multilswap_contract = w3.eth.contract(address = multilswap, abi= multilswap_abi)

# amountIn = optimalAmount

def dataswap_encode(contract, amountIn, amountOut, path, mycontract):
	deadline = 1000
	dataswap = contract.encodeABI(fn_name="swapExactTokensForTokens", args=[amountIn,amountOut, path, mycontract,deadline])
	return dataswap

def dataswap(route,tokenIn, tokenOut, amountIn, mycontract):
	# route = trade['route']
	tos = []
	tos = [t['router:'] for t in route]
	data = []
	_tokenInapproveaddr = []
	n= 0 
	for pair in route:

		if pair['router:'] == '0x145863Eb42Cf62847A6Ca784e6416C1682b1b2Ae':
			contract = VVS_ROUTER_CONTRACT
		elif pair['router:'] == '0x145677FC4d9b8F19B5D56d1820c48e0443049a30':
			contract = MMF_ROUTER_CONTRACT
		elif pair['router:'] == '0xcd7d16fB918511BF7269eC4f48d61D79Fb26f918':
			contract = CRONA_ROUTER_CONTRACT
		elif pair['router:'] == '0x5bFc95C3BbF50579bD57957cD074fa96a4d5fF9F':
			contract = CYBORG_ROUTER_CONTRACT

		if n == 0:
			amountIn = amountIn
			if pair['token0']['address'] == tokenIn['address']:
				tokenOut = pair['token1']
			else:
				tokenOut = pair['token0']
			path = [tokenIn['address'],tokenOut['address']]
			_tokenInapproveaddr.append(tokenIn['address'])
			amountOut_list = contract.functions.getAmountsOut(amountIn, path).call()
			amountOut= amountOut_list[1]
			print('amountout1:',amountOut)
			encode = dataswap_encode(contract, amountIn, amountOut, path, mycontract)
			data.append(encode)
			# approve = 
			tokenIn = tokenOut
			amountIn = amountOut
		
		if n > 0:

			if pair['token0']['address'] == tokenIn['address']:
				tokenOut = pair['token1']
			else:
				tokenOut = pair['token0']
			path = [tokenIn['address'],tokenOut['address']]
			_tokenInapproveaddr.append(tokenIn['address'])
			amountOut_list = contract.functions.getAmountsOut(amountIn, path).call()
			amountOut= amountOut_list[1]
			print('amountout2:',amountOut)
			encode = dataswap_encode(contract, amountIn, amountOut, path, mycontract)
			data.append(encode)
			# approve = 
			tokenIn = tokenOut
			amountIn = amountOut
		n+=1
	print('profit:', amountIn - 50*pow(10,18))
	return tos, data, _tokenInapproveaddr


	



