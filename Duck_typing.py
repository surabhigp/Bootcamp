class Student:
    def learn(self):
        print("This is student")

class Trainer:
    def guide(self):
        print("this is trainer")


person1 = Student()
person2 = Trainer()

def check_behv(take_person):
    take_person.learn()
    take_person.guide()
  

check_behv(person1)