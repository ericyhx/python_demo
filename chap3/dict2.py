# auth:eric.yu
# date: 2023/7/24 17:23
d={'zhangsan':34,'lisi':34}
print(d['zhangsan'])
print(d.get('zhangsan1',57))
print('zhangsan' not in d)
print('zhangsan' in d)
del d['zhangsan']
print('zhangsan' not in d)
print('zhangsan' in d)
d.clear()
print(d)
d['chenliu']=98
print(d)
d['chenliu']=100
print(d)
d['mawu']=100
print(d)
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(list(d.items())) #元组
for item in d:
    print(item,d.get(item))
