

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(self.name,self.age)
    def __str__(self):
        return f'我的名字{self.name},我今年{self.age}岁'


class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachYears):
        super().__init__(name,age)
        self.teachYears=teachYears

stu=Student("zhangsan",20,1001)
teacher=Teacher("wangwu",50,10)
stu.info()
teacher.info()
print(stu)
print(dir(stu))
