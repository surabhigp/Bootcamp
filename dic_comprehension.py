dic6 = {0:{5:10}, 1:{}, 2:7, 3:6}
dic = {k:v for k,v in dic6.items() if type(v)==type(dic6)}


prices = {'P11':{1:200}, 'P22': {2:200}, 'P33': 76, 'P44': 765}
print(type(prices))
dict_sub = {key:value for key,value in prices.items() if type(value)==dict}

print(dict_sub)
