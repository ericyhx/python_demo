# auth:eric.yu
# date: 2023/7/28 11:17
'''
静态语言实现多态的三个必要条件：
    继承
    方法重写
    父类引用指向子类引用
动态语言的多态
    崇尚‘鸭子类型’，当看到一只鸟走起路来像鸭子、游泳起来像鸭子、收起来也像鸭子，
    那么这只鸟可以北称为鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，
    只关心对象的行为
'''

class Animal():
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头。。。")
class Cat(Animal):
    def eat(self):
        print("猫喜欢吃鱼")
class Person():
    def eat(self):
        print("人可以吃动物")
def eatFunc(animal):
    animal.eat()

eatFunc(Cat())
eatFunc(Dog())
eatFunc(Person())
eatFunc(Animal())

