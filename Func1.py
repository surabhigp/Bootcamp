#functions

#   def function_name():
#       function_body/Logic
#
#   function_call()

def show():
    print('this is 1st function')


show()

#para functions
def para_fun(num1, num2):
    print(num1, num2)


para_fun(10, 20)
para_fun('Guido', 'Python')

def para_fun_two(num1, num2):
    print(num1)
    print(num2)


para_fun_two(num2 = 50, num1 = 100)

#default value
def para_fun_three (num1, num2=20):
    print(num1-num2)

para_fun_three(100)
para_fun_three(100,30)

#throws error
#def para_fun_four (num1=50, num2 ):
#    print(num1+num2)

#para_fun_four(100)
#error
#C:\Users\Admin\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\Admin\PycharmProjects\pythonProject\Func1.py
#  File "C:\Users\Admin\PycharmProjects\pythonProject\Func1.py", line 37
#   def para_fun_four (num1=50, num2):

#SyntaxError: non-default argument follows default argument

#function inside function
def outer_fun():
    print("this is outer function")
    def inner_fun():
        print("this is inner function ")

    inner_fun()
outer_fun()

#need to return the addition
def nfun_outer(num1, num2):
    def nfun_inner():
        return num1+num2

    return nfun_inner()
print(nfun_outer(30,40))

