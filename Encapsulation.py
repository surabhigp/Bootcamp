#encapsulation: data binding + privacy (public, private, proctected)
#                                       access modifiers or specifiers
#             : var, methods

class Myclass:
    #by default public
    my_num = 7
    #protected: underscore(_) represents protected member
    _name = 'Python'
    #private: double underscore(__) represents private member
    __age = 24
    def access_private_mem(self):
        print(self.__age)

obj = Myclass()
print(obj.my_num)
print(obj._name)
#print(obj.__age)
#AttributeError: 'Myclass' object has no attribute '__age': error
obj.access_private_mem()