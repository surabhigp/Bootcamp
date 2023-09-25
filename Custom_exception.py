#----------program 15--------
#custom exception
# raise keyword--> obj creation of exception kind of classes
#part1
#absent = 8

#if absent >6:
#    raise ZeroDivisionError("Terminated")
#    print("Can not connect to zoom")#This code is unreachable
#
#else:
#    print("You can continue with training")

#---------program 16------------
#part2
#class AbsentException(BaseException):
#    def __init__(self,error_msg):
 #       print(error_msg)

#absent = 8

#if absent > 6:
#    raise AbsentException("Terminated")
#
#else:
#    print("You can continue with training")

#------------program 17---------
#part 3
class AbsentException:
    def __init__(self, error_msg):
        super().__init__(error_msg)

absent = 8

if absent > 6:
    raise AbsentException("Terminated")

else:
    print("You can continue with training")
