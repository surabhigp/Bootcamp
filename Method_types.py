# 3 types of Methods
class MethodType:
    id =1

    def instance_method(self):
        print("this is instance method")

    @staticmethod
    def static_method():
        print("this is static method")

    # can chnage the attributes of the static variable
    # cls --> behind takes className
    @classmethod
    def class_method(cls):
        print("this is class method")
        cls.id = 2

MethodType.static_method()
print(MethodType.id)
MethodType.class_method()
print(MethodType.id)


obj1 = MethodType()
obj1.instance_method()

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return self.fname + self.lname

p1 = Person("Surabhi", "Panchal")
p2 = Person("S", "P")
print(p1)
print(p2)