# auth:eric.yu
# date: 2023/7/24 17:54

t=(10,[20,30],40)
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
t[1].append(50)
print(t[1],type(t[1]),id(t[1]))


for i in t:
    print(i)
