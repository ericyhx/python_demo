# auth:eric.yu
# date: 2023/7/31 11:33
year=[82,84,83,96,98,00,73]
print('原列表：',year)
for index,value in enumerate(year):
    if str(value) != '0':
        year[index] = '19'+str(value)
    else:
        year[index] = '200' + str(value)
print("修改后：",year)
year.sort()
print('排序后：',year)
