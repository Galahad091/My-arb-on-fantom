from decimal import Decimal

tokenIn ={
            'address': '0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23',
            'symbol': 'WCRO',
            'decimal': 18,
            }
            
tokenOut = {
            'address': '0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23',
            'symbol': 'WCRO',
            'decimal': 18,
            }
maxHops = 5
amountIn = 1
currentPairs = []
path = [tokenIn]
origToken = tokenIn
origAmount = amountIn
bestTrades = None


currentPairs1 = [{'index': 4, 'address': '0xe61Db569E231B3f5530168Aa2C9D50246525b6d6', 'token0': {'address': '0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23', 'symbol': 'WCRO', 'decimal': 18}, 'token1': {'address': '0xc21223249CA28397B4B6541dfFaEcC539BfF0c59', 'symbol': 'USDC', 'decimal': 6}, 'reserve0': 119502016000000000000000000, 'reserve1': 18070132000000, 'router:': '0x145863Eb42Cf62847A6Ca784e6416C1682b1b2Ae', 'r1': 0.997, 'r2': 1}, {'index': 241, 'address': '0x40EB90721114a0A10eD7732F4dCB74D9672A9FcD', 'token0': {'address': '0xc21223249CA28397B4B6541dfFaEcC539BfF0c59', 'symbol': 'USDC', 'decimal': 6}, 'token1': {'address': '0xEfA1FABC2AB6219174aD1c912F56f7de53cDc1E1', 'symbol': 'DARKCRYSTL', 'decimal': 18}, 'reserve0': 5671280000, 'reserve1': 40615000000000000000000, 'router:': '0x145677FC4d9b8F19B5D56d1820c48e0443049a30','r1': 0.9983, 'r2': 1}, {'index': 229, 'address': '0x59505978Dcdb0c820ECf6486AFEB9b2Baa58Ff49', 'token0': {'address': '0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23', 'symbol': 'WCRO', 'decimal': 18}, 'token1': {'address': '0xEfA1FABC2AB6219174aD1c912F56f7de53cDc1E1', 'symbol': 'DARKCRYSTL', 'decimal': 18}, 'reserve0': 81716000000000000000000, 'reserve1': 83995000000000000000000, 'router:': '0x145677FC4d9b8F19B5D56d1820c48e0443049a30','r1': 0.9983, 'r2': 1}]

RWCRO_USDC = 119502016000000000000000000
RUSDC_WCRO = 18070132000000
RUSDC_DARKCRYSTL = 5671280000
RDARKCRYSTL_USDC = 40615000000000000000000
RDARKCRYSTL_WCRO = 83995000000000000000000
RWCRO_DARKCRYTL = 81716000000000000000000
def getOptimalAmount(pairs,Ea, Eb):
    if Ea > Eb:
        return None
    if not isinstance(Ea, Decimal):
        Ea = Decimal(Ea)
    if not isinstance(Eb, Decimal): 
        Eb = Decimal(Eb)
    return Decimal(int((Decimal.sqrt(Ea*Eb*Decimal(pairs[0]['r1'])*Decimal(pairs[0]['r2']))-Ea*Decimal(pairs[0]['r2']))/Decimal(pairs[0]['r1']))) 

def adjustReserve(token, amount):
    # res = Decimal(amount)*Decimal(pow(10, 18-token['decimal']))
    # return Decimal(int(res))
    return amount

def toInt(n):
    return Decimal(int(n))

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
            Ra = pairs[0]['reserve0'] #adjustReserve(pairs[0]['token0'], pairs[0]['reserve0'])
            Rb = pairs[0]['reserve1'] #adjustReserve(pairs[0]['token1'], pairs[0]['reserve1'])
            if tokenIn['address'] == pairs[0]['token1']['address']:
                temp = Ra
                Ra = Rb
                Rb = temp
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

Ea, Eb = getEaEb(tokenOut, currentPairs1)
print('Ea:',Ea)
print('Eb:',Eb)
print('Ea-Eb:',Ea - Eb)
if Ea < Eb:
    print('profitable')
else:
    print('no profitable')

optimal = getOptimalAmount(currentPairs1, Ea, Eb)
print('optimal amount is:', optimal)