def outer():
    def inner():
        print('inner function')

    return inner
outer()

inner_ref_collector = outer()
inner_ref_collector()


#lamda functions
#when u want to pass the arguments

#traditional approach
def intofive(num):
     return num * 5

print( intofive(10))

#lambda approach
new_fun = lambda num : num*5
print(new_fun(7))

add = lambda num1 , num2 : num1+num2
print(add(10,20))


#best case senioro
def o_nfun(num1):
    return lambda : num1*num1

collertor_inner_fun = o_nfun(7)
print(collertor_inner_fun())