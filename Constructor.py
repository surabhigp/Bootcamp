class Home:
    room = 2
    kitchen = 1

person1 = Home()
person2 = Home()

print(person1.room)
print(person1.kitchen)

print(person2.room)
print(person2.kitchen)


class Home1:
    def __init__(self, count_of_room, count_of_kitchen):
        self.room = count_of_room
        self.kitchen = count_of_kitchen

#object initailization
person1 = Home1(3,1)
person2 = Home1(2,1)

print(person1.room)
print(person1.kitchen)

print(person2.room)
print(person2.kitchen)



class Home:
    #left side var --> instance varailable --> can be access via object only
    #by default variables are --> static variable in python ---> access via class on;y
    # instance --> object

    def __int__(self,room,kitchen):
        self.room = room
        self.kitchen = kitchen

person1 = Home()
person2 = Home(2,1)

print(person1.room)
person1.room = 10
print("after change")
print(person1.room)
print(person2.room)


class Home:
    # static varaible belongs to classes
    # gets memory allocated at class loading time
    room = 2
    kitchen = 1

print(Home.room)
print(Home.kitchen)

h1 = Home()
h2 = Home()

#do not access it like this
print(h1.room)
print(h2.room)

#do not manipulate it like this
h1.room = 5
print(h1.room)
print(h2.room)

# manipulate it like this
print(Home.kitchen)
Home.kitchen = 3
print(Home.kitchen)

print(h1.kitchen)
print(h2.kitchen)


