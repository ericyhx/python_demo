# auth:eric.yu
# date: 2023/7/28 10:24

class Student:
  native_city='shanghai'
  def __init__(self,name,age):
      self.name=name
      self.__age=age
  def eat(self):
      print("正在 吃饭")
  @staticmethod
  def method():
      print("这是静态方法")
  @classmethod
  def clsMethod(self):
      print("这是类静态方法")


stu=Student("张三十四",20)
print("1",stu.name)
# print(stu.__age)
Student.method()
stu.eat()
stu.method()
stu.clsMethod()
Student.clsMethod()
