# abstraction: data hiding + show case necessary details to users
#example:
#Laptop [ram,hdd,motherboard,(screen, keyboard)]
# car [gear,engine]

#abstract class:
#   ---->can't create object

#abstract method:
#   ----> without body
#   ----> need to implement in child class
#   ---->only inside abstrct class
# class--> abstract class,

from abc import ABC, abstractmethod

class Absclass(ABC):
    def simple_method(self):
        print("simple method")

    @abstractmethod
    def abs_method(self):
        pass

#obj = AbsClass()
#obj.simple_method()

class Mychild(Absclass):
    def abs_method(self):
        print("abs method")

obj = Mychild()
obj.simple_method()
obj.abs_method()

#GETTER SETTERS METHOD IN PYTHON & what is the way to implement it with example