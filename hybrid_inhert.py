#consisting of multiple types of inheritance is called hybrid inheritance.
# hybrid inheritance


class Parent:
    def parent(self):
        print("This method is parent.")


class Child1(Parent):
    def child1(self):
        print("This mrthod is in child 1. ")


class Child2(Parent):
    def child2(self):
        print("This method is in child 2.")


class Child3(Child1, Parent):
    def child3(self):
        print("This method is in child 3.")



object = Child3()
object.parent()
object.child1()
object.child3()


obj = Child2()
obj.child2()
obj.parent()