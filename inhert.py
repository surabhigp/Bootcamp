# inheritance
# -- Reusability
# type -- single, multilevel,hirc, multiple, hybrid

# syntax
# CPP:class child : parent
# Java/C# class Child extends parent
# python: class Child(Parent)

# --- Single ---
print("Single inhertance")
class Parent:
    def parent_method(self):
        print("this is parent feature")

class Child(Parent):
    def child_method(self):
        print("this is child feature")


ch = Child()
ch.child_method()
ch.parent_method()
#constructure --> obj init
#child obj --> real time -->without parent

class P1:
    def __init__(self):
        print("this is parent 1")

class C1(P1):
    def __init__(self):
        print("this is child 1")

ch = C1()

class P2:
    def __init__(self):
        print("this is parent 2")

class C2(P2):
    def __init__(self):
        super().__init__()
        print("this is child 2")

ch1 = C2 ()
#what is we call super in some other section of init of child

class P3:
    def __init__(self):
        print("this is parent 3")

class C3(P3):
    def __init__(self):
        print("this is child 3")
        super().__init__()

ch2 = C3()

# this code will throw an runtime error
class P4:
    def __init__(self,pname):
        self.pname = pname

class C4(P4):
    def __init__(self):
        print("this is Child 4")

ch3 = C4()

# Surabhi G Panchal
class P5:
    def __init__(self, pname):
        self.pname = pname

class C5(P5):
    def __init__(self):
        super().__init__("SGP")
        print("this is C5")

ch4 = C5()
print(ch4.pname)

# --- Multilevel ---
print("Multilevel inhertance")

class GParent:
    def gparent_methos(self):
        print("this is grand parent class")

class Parent1(GParent):
    def parent1_method(self):
        print("this is parent class")

class Child1(Parent1):
    def child1_methos(self):
        print("this is child feature")

ch = Child1()
ch.child1_methos()
ch.parent1_method()
ch.gparent_methos()


# --- Hirc ---
#When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
print("Hirchical inhertance")
class Parent2:
    def parent2_method(self):
        print("this is Parent2")

class Child_one(Parent2):
    def child_one_method(self):
        print("this is child_one of hirechical inhertance")

class Child_two(Parent2):
    def child_two_method(self):
        print("this is child two of hirarchical inhertance")

ch = Child_one()
chi = Child_two()

ch.child_one_method()
ch.parent2_method()

chi.child_two_method()
chi.parent2_method()


# --- Multiple Parent child 1 ---
print("Multiple inhertance")


# -- Multiple Part 1---

class Parent_one:
    def parent_one_method(self):
        print("parent")

class Parent_two:
    def parent_two_method(self):
        print("second parent")

#java, C# -->not allowed
#c++, python -->allowed
class Child_H(Parent_one,Parent_two):
    def child_H(self):
        print("this is child of hirarchical inhertance")

chi1 = Child_H()
chi1.parent_one_method()
chi1.parent_two_method()
chi1.child_H()

#-------Multiple part 2---------

class Parent_multiple:
    def parent_multiple(self):
        print("this is parent of multiple inheritannce")

class Parent_two:
    def parent_two_method(self):
        print("this is parent 2 of multiple inherite=ance")

class Child_multiple(Parent_multiple,Parent_two):
    def child_multiple(self):
        print("this is child of multiple")

ch5 = Child_multiple()
ch5.parent_multiple()
ch5.parent_two_method()
ch5.child_multiple()
# --- hybrid ---
print("Hybrid inhertance")
