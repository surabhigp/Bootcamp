#Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class
def uppercase_decor(function1):
    def wrap1():
        func = function1()
        makeuppercase = func.upper()
        return makeuppercase

    return wrap1

def hi():
    return "hello"

decorate = uppercase_decor(hi)
print(decorate())

@uppercase_decor
def hi():
    print("Enter your name")
    x = input()
    return 'hi' + x

print(hi())