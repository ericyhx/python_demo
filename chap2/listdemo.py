# auth:eric.yu
# date: 2023/7/24 16:08


lst = [10,20,30]
print("添加之前",lst,id(lst))
lst.append(40)
print("添加之后",lst,id(lst))
lst2=['hello','world']
# lst.append(lst2)
lst.extend(lst2)
print(lst)
lst.insert(1,50)
print(lst)
lst3=[True,False,'helloworld']
lst[1:5]=lst3
print(lst)
print('-------------切片-------------')

