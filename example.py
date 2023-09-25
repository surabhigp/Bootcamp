class Person:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
    #__str__(self): can also be used
    def __repr__(self):
        return self.fname + self.lname

p1 = Person("Ayush", "Verma")
p2 = Person("Surabhi", "Panchal")
print(p1)
print(p2)

#Intel
#nvidia
#corsair

#kalyan -> 8ram, 8graphic, i9proces
#jayanth -> 16ram, 2graphic, i7proces

class Laptop:
    def __init__(self, core, gcard, processor):
        self.core = core