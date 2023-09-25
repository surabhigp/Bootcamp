class Home:
    # static variable belongs to classes
    # gets memory allocated at class loading time
    #shared memory for every objecy
    room = 2
    kitchen = 1

print(Home.room)
print(Home.kitchen)

h1 = Home()
h2 = Home()

#constructor
#1: Will get call automatically
#2: Will get called at object creation time & seprate fpr each object
#3: We cant call constructor
#4: No retyrn statement inside __init__()
#5: __init__() is

class Home:
    #no constructor but special method
    def __int__(self):
        print("this is special method")

h1 = Home()
h2 = Home()

Home.__int__(h1)


#-------------------------

# cannot work this way: assigning varaible after the class is created is not right way to writr the code
class Home:
    pass

h1 = Home()
h1.name = "Surabhi"
print(h1.name)