

#OPIMIZE ROUTE: Gộp các router giống nhau swap liền nhau lại, tránh swap nhiều lần trên cùng 1 dex

# def optimize_route(trade):
#     trade = trade['route']
#     router = []
#     path = []
#     n = 0
#     for i in range(len(trade)):
#         if i == 0:
#             router.append(trade[i]['router:'])
#             if trade[i]['token0']['address'] == tokenIn['address']:
#                 path1 = [trade[i]['token0']['address'], trade[i]['token1']['address']]
#             elif trade[i]['token1']['address'] == tokenIn['address'] :
#                 path1 = [trade[i]['token1']['address'], trade[i]['token0']['address']]
#             path.append(path1)
        
#         elif i > 0 and trade[i]['router:'] == trade[i-1]['router:']:
#             if trade[i]['token0']['address'] == path[n][-1]:
#                 path[n].append(trade[i]['token1']['address'])
#             elif trade[i]['token1']['address'] == path[n][-1]:
#                 path[n].append(trade[i]['token0']['address'])

#         elif i > 0 and trade[i]['router:'] != trade[i-1]['router:']:
#             path2 = []
#             router.append(trade[i]['router:'])
#             if trade[i]['token0']['address'] == path[n][-1]:
#                 path2 = [trade[i]['token0']['address'], trade[i]['token1']['address']]
#             elif trade[i]['token1']['address'] == path[n][-1]:
#                 path2 = [trade[i]['token1']['address'], trade[i]['token0']['address']]
#             path.append(path2)
#             n+=1
#     return router, path 




