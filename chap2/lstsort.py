# auth:eric.yu
# date: 2023/7/24 16:38

lst=[10,20,40,50,30,80,60]

lst.sort()
print(lst)
lst.sort(reverse=1)
print(lst)
print("---------使用内置函数-------------")
lst2=[10,20,40,50,30,80,60]

new_lst=sorted(lst2,reverse=True)
print('原列表',lst2,id(lst2))
print('排序后列表',new_lst,id(new_lst))

