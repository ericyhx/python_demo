# auth:eric.yu
# date: 2023/7/26 16:25

s1={10,20,30,40}
s2={30,40,20,10}
print(s1==s2)
s1={10,20,30,40,50,60}
s2={30,40,20,10,5}
print(s2.issubset(s1)) #子集
print(s1.issuperset(s2)) #超集
print(s1.isdisjoint(s2)) #是否没有交集
#集合的数学操作
##1、求交集
print(s1.intersection(s2))
print(s1 & s2)
##2、求并集
print(s1.union(s2))
print(s1 | s2)
##3、求差集
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
##4、求对称差集
print(s1.symmetric_difference(s2))
