import json
from dfs import*
from router import*
from decimal import Decimal
from thread import *
import threading
from events import*
import random

#FUNCTIONS FIND ARBITRAGE OPPORTUNITY

#get Optimal Input
def getOptimalAmount(pairs,Ea, Eb):
    if Ea > Eb:
        return None
    if not isinstance(Ea, Decimal):
        Ea = Decimal(Ea)
    if not isinstance(Eb, Decimal): 
        Eb = Decimal(Eb)
    return Decimal(int((Decimal.sqrt(Ea*Eb*Decimal(pairs[0]['r1'])*Decimal(pairs[0]['r2']))-Ea*Decimal(pairs[0]['r2']))/Decimal(pairs[0]['r1']))) 

# def adjustReserve(token, amount):
#     # res = Decimal(amount)*Decimal(pow(10, 18-token['decimal']))
#     # return Decimal(int(res))
#     return amount
def randSelect(allp, num=0):
    maxNum = len(allp)
    start = random.randint(0, maxNum-num)
    return allp[start:start+num]

def toDict(pairs):
    p = {}
    i = 0
    for pair in pairs:
        p[pair['address']] = pair
        p[pair['address']]['arrIndex'] = i
        i += 1
    return p

#get lastest reserve (>200 pairs)
# needChangeKey = False
# def threadpair(pairs):
#     s = 0
#     threads = []
#     while s < len(pairs): 
#         e = s + 50
#         if e > len(pairs):
#             e = len(pairs)
#         t = MyThread(func = get_reserves, args=(pairs[s:e],))
#         t.start()
#         threads.append(t)
#         s = e
#     new_pairs = []
#     for t in threads:
#         t.join()
#         ret = t.get_result()
#         if not ret:
#             needChangeKey = True
#         new_pairs.extend(ret)
#     return new_pairs

def toInt(n):
    return Decimal(int(n))

#get Ea,Eb
def getEaEb(tokenIn, pairs):
    Ea = None
    Eb = None
    idx = 0
    tokenOut = tokenIn.copy()
    for pair in pairs:
        if idx == 0:
            if tokenIn['address'] == pair['token0']['address']:
                tokenOut = pair['token1']
            else:
                tokenOut = pair['token0']
        if idx == 1:
            # Ra, Rb = get_reserves(pairs[0])
            Ra = pairs[0]['reserve0'] #adjustReserve(pairs[0]['token0'], pairs[0]['reserve0'])
            Rb = pairs[0]['reserve1'] #adjustReserve(pairs[0]['token1'], pairs[0]['reserve1'])
            if tokenIn['address'] == pairs[0]['token1']['address']:
                temp = Ra
                Ra = Rb
                Rb = temp
            # Rb1, Rc = get_reserves(pair)
            Rb1 = pair['reserve0'] #adjustReserve(pair['token0'], pair['reserve0'])
            Rc = pair['reserve1'] #adjustReserve(pair['token1'], pair['reserve1'])
            if tokenOut['address'] == pair['token1']['address']:
                temp = Rb1
                Rb1 = Rc
                Rc = temp
                tokenOut = pair['token0']
            else:
                tokenOut = pair['token1']
            Ea = toInt(Decimal(pair['r2'])*Ra*Rb1/(Decimal(pair['r2'])*Rb1 + Decimal(pair['r1'])*Rb))
            Eb = toInt(Decimal(pair['r1'])*Rb*Rc/(Decimal(pair['r2'])*Rb1 + Decimal(pair['r1'])*Rb))
        if idx > 1:
            Ra = Ea
            Rb = Eb
            # Rb1, Rc = get_reserves(pair)
            Rb1 = pair['reserve0'] #adjustReserve(pair['token0'], pair['reserve0'])
            Rc = pair['reserve1'] #adjustReserve(pair['token1'], pair['reserve1'])
            if tokenOut['address'] == pair['token1']['address']:
                temp = Rb1
                Rb1 = Rc
                Rc = temp
                tokenOut = pair['token0']
            else:
                tokenOut = pair['token1']
            Ea = toInt(Decimal(pair['r2'])*Ra*Rb1/(Decimal(pair['r2'])*Rb1 + Decimal(pair['r1'])*Rb))
            Eb = toInt(Decimal(pair['r1'])*Rb*Rc/(Decimal(pair['r2'])*Rb1 + Decimal(pair['r1'])*Rb))
        idx += 1
    return Ea, Eb

#get amount out
def getAmountOut(pairs,amountIn, reserveIn, reserveOut):
    assert amountIn > 0
    assert reserveIn > 0 and reserveOut > 0
    if not isinstance(amountIn, Decimal):
        amountIn = Decimal(amountIn)
    if not isinstance(reserveIn, Decimal):
        reserveIn = Decimal(reserveIn)
    if not isinstance(reserveOut, Decimal):
        reserveOut = Decimal(reserveOut)
    return Decimal(pairs[0]['r1'])*amountIn*reserveOut/(Decimal(pairs[0]['r2'])*reserveIn+Decimal(pairs[0]['r1'])*amountIn)



#APPROVE 

#DO TRADE


