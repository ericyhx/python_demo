# auth:eric.yu
# date: 2023/7/31 11:01
import  random
rand=random.randint(1,100)
for i in range(1,11):
    num=int(input('在我心中有个数1-100，请你猜一猜:'))
    if num<rand:
        print('小了')
    elif num>rand:
        print('大了')
    else:
        print('恭喜你才对了！')
        break
print(f'您一共猜了{i}次')
if i <3:
    print('真聪明')
elif i<=7:
    print('还凑合')
else:
    print('天哪，你真笨^_^')
