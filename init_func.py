#class Home:
#    room = 2
#    kitchen = 1


#person1 = Home()
#person2 = Home()
#print(person1.room)
#prinr(person1.kitchen)

class Home:
    def __init__(self,count_of_room,count_of_kitchen):
        self.room = count_of_room
        self.kitchen = count_of_kitchen

#object init
#person1 = Home(3,1)
#person2 = Home(2,1)

#print(person1.room)
#print(person1.kitchen)

#print(person2.room)
#print(person2.kitchen)

#class Home:
    def __init__(self,room,kitchen):
        self.room = room
        self.kitchen = kitchen

person1 = Home(4,2)
person2 = Home(3,1)

print(person1.room)
person1.room = 10
print("After change")
print(person1.room)
print(person2.room)
print(person2.kitchen)

class Home:
    room = 2
    kitchen = 1

print(Home.room)
print(Home.kitchen)
h1 = Home()
h2 = Home()

print(h1.room)
print(h2.room)

h1.room = 5
print(h1.room)
print(h2.room)

print(Home.kitchen)
Home.kitchen = 3
print(Home.kitchen)

print(h1.kitchen)
print(h2.kitchen)

class Home:
    room =1
    kitchen = 1


print(Home.room)
print(Home.kitchen)
h1 = Home()
h2 = Home()

class Home:
    def __init__(self):
        print("this is special method")


h1.home()
h2.home()

class Home:
    pass

#h1 = Home()
#h1.name = "Surabh"
print(h1.name)