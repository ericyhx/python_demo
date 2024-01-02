# auth:eric.yu
# date: 2023/7/26 17:00

s="hello|world|python"
print(s.split())
print(s.split(sep="|"))
print(s.split(sep="|",maxsplit=1))
print(s.rsplit(sep="|"))
print(s.rsplit(sep="|",maxsplit=1))
###############字符串判断的方法##################
print("1",s.isidentifier())
print("2",'hello'.isidentifier())
print("3",'张三_'.isidentifier())
print("4",'张三_123'.isidentifier())

#是否是空白字符
print("5",'\t'.isspace())

#是否全部有字母组成
print("6",'abc'.isalpha())
print("7",'张三'.isalpha())
print("8",'张三1'.isalpha())
#是否全部由10进制组成
print("9",'123'.isdecimal())
print("10",'123四'.isdecimal())
#是否全部有数字组成
print("11",'123'.isnumeric())
print("12",'123四'.isnumeric())
#是否全部由字母和数字组成
print("13",'abc123'.isalnum())
print("14",'张三123四'.isalnum())
print("15",'abc!'.isalnum())

###############字符串替换的方法##################
s = "hello python"
print(s.replace("python","java"))
#列表
lst=["hello","java","python"]
print("|".join(lst))
print(" ".join(lst))
#元组
t=("hello","java","python")
print("@".join(t))
print("*".join("python"))
