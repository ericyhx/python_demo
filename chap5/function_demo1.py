# auth:eric.yu
# date: 2023/7/26 17:57


#1、个数可变的位置参数，只能定义一个，结果是一个元组
def fun(*args):
    print(args)
fun(10)
fun(10,20)
fun(10,20,30,40)
#2、个数可变的关键字形参，只能定义一个，结果是一个字典
def fun1(**args):
    print(args)
fun1(a=10)
fun1(b=20,c=30)
fun1(a=40,b=50,c=60)
#3、在一个函数的定义过程中，既有个数可变的位置参数，又有个数可变的关键字形参，个数可变的位置参数一定要放在个数可变的关键字形参前面
print("-----------------------------")
def fun3(a,b,c):
    print('a=',a)
    print('b=', b)
    print('c=', c)
fun3(10,20,30) #位置实参传递
lst=[10,20,30]
fun3(*lst)

fun3(a=100,c=200,b=300) #关键字实参传递
dic={'a':100,'b':300,'c':200}
fun3(**dic)

#从*之后的参数只能采用关键字传递
def fun4(a,b,*,c,d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
# fun4(10,20,30,40) #会报错，后面两位没有按照关键字传递
fun4(10,20,c=30,d=40)


'''函数定义时的形参的顺序问题'''
def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args1,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass
