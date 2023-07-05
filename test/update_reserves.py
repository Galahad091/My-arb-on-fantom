import json
from decimal import Decimal
# add your blockchain connection information
from router import*
from thread import *
import threading
from lookevents import*
#get reserve
# pairs = json.load(open('pairs_dexscreener.json'))
# def get_reserves_pairs(pairs):
#     for pair in pairs:
#         if pair['router:'] == '0x145863Eb42Cf62847A6Ca784e6416C1682b1b2Ae':
#             pair_addr_crc = Web3.toChecksumAddress(pair['address'])
#             pair_contract = w3.eth.contract(address=pair_addr_crc, abi= VVS_PAIR_ABI)
#             reserves = pair_contract.functions.getReserves().call()
#             pair['reserve0'] = reserves[0]
#             pair['reserve1'] = reserves[1]

#         elif pair['router:'] == '0x145677FC4d9b8F19B5D56d1820c48e0443049a30':
#             pair_addr_crc = Web3.toChecksumAddress(pair['address'])
#             pair_contract = w3.eth.contract(address=pair_addr_crc, abi= MMF_PAIR_ABI)
#             reserves = pair_contract.functions.getReserves().call()
#             pair['reserve0'] = reserves[0]
#             pair['reserve1'] = reserves[1]
#         elif pair['router:'] == '0xcd7d16fB918511BF7269eC4f48d61D79Fb26f918':
#             pair_addr_crc = Web3.toChecksumAddress(pair['address'])
#             pair_contract = w3.eth.contract(address=pair_addr_crc, abi= CRONA_PAIR_ABI)
#             reserves = pair_contract.functions.getReserves().call()
#             pair['reserve0'] = reserves[0]
#             pair['reserve1'] = reserves[1]
#         elif pair['router:'] == '0x5bFc95C3BbF50579bD57957cD074fa96a4d5fF9F':
#             pair_addr_crc = Web3.toChecksumAddress(pair['address'])
#             pair_contract = w3.eth.contract(address=pair_addr_crc, abi= CYBORG_PAIR_ABI)
#             reserves = pair_contract.functions.getReserves().call()
#             pair['reserve0'] = reserves[0]
#             pair['reserve1'] = reserves[1]
#     return pairs 

needChangeKey = False
def threadpair(pairs):
    s = 0
    threads = []
    while s < len(pairs): 
        e = s + 30
        if e > len(pairs):
            e = len(pairs)
        t = MyThread(func = get_reserves, args=(pairs[s:e],))
        t.start()
        threads.append(t)
        s = e
    new_pairs = []
    for t in threads:
        t.join()
        ret = t.get_result()
        if not ret:
            needChangeKey = True
        new_pairs.extend(ret)
    return new_pairs




