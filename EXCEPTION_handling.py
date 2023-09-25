#--------Exception Handling------------
#Exception--> compile time error, runtime error: we must handle it
#Error--> syntax, compile, runtime --> willingly dont want to handle
#Bug--> unexcpected output
#----------program 1-------
print("Start")
print("Line 1")

try:
    print("Line 2", 100/0)

except:
    print("please dont divide by 0")

print("Line 3")
print("End")

#----------------program 2----------
print("Start")
print("Line 1")

try:
    print("Line 2", 100/0)

except Exception as e:
    print(e)

print("Line 3")
print("End")

#----------program 3--------
print("Start")
print("Line 1")

num1 = int(input("enter num1."))
num2 = int(input("enter num2."))
try:
    result = num1/ num2
    print(result)

except Exception as e:
    print(e) or print("dont use 0 for division")

print("Line 3")
print("End")

#------------progrom 4----------
print("Start")
print("Line 1")

num1 = int(input("enter num1."))
num2 = int(input("enter num2."))
try:
    result = num1/ num2
    print(result)

except Exception as e:
    num2 =2
    print("your given no was ", num1)
    print("we have interchanged the value for num2 with 1")
    print(num1 / num2)
print("Line 3")
print("End")

#---------Program 5--------------------
# try ----> multi except
print("Start")
print("Line 1")


try:
    print(25 / 0)

except ZeroDivisionError as e:
    print("Block1")

except Excep1tion as e:
    print("block2")

print("Line 3")
print("End")

#----------program 6-----------
# in multi exception--> specific to generic exception classes
print("Start")
print("Line 1")


try:
    print(25 / 0)

except Exception as e:
    print("block2")

except ZeroDivisionError as e:
    print("Block1")


print("Line 3")
print("End")

#-----------------Program 7---------
#--- try ---> try except followed by except
print("Start")
print("Line 1")


try:
    print(25 / 0)
    try:
        print(50/2)

    except ZeroDivisionError as e:
        print("Inner Block")

except Exception as e:
    print("outer block")

print("Line 3")
print("End")

#-------------- program 8------------
print("Start")
print("Line 1")


try:
    print(25 / 5)
    try:
        print(50/0)

    except ZeroDivisionError as e:
        print("Inner Block")
        print(100/0)

except Exception as e:
    print("outer block")

print("Line 3")
print("End")

#----------program 9-----------
print("Start")
print("Line 1")


try:
    li1 = [1,2,3,4,5]
    print(li1[5]/0)


except IndexError as e:
    print("block 1")

except Exception as e:
    print("block 2")
print("Line 3")
print("End")

#------ program 10---------
#try---> except--->finally
#without exception
print("Start")
print("Line 1")


try:
    li1 = [1,2,3,4,5]
    print(li1[3]/2)


except IndexError as e:
    print(e)

finally:
    print("Always executed")


print("Line 3")
print("End")

# ------ program 11---------
# try--->except----->finally
# with exception
print("Start")
print("Line 1")

try:
    li1 = [1, 2, 3, 4, 5]
    print(li1[5] / 2)

except IndexError as e:
    print(e)

finally:
    print("Always executed")

print("Line 3")
print("End")

#-----------program 12---------
# try--->finally
# with exception
print("Start")
print("Line 1")

try:
    li1 = [1, 2, 3, 4, 5]
    print(li1[5] / 2)

finally:
    print("Always executed")

print("Line 3")
print("End")


#-----------program 13---------
# try--->finally
# without exception
print("Start")
print("Line 1")

try:
    li1 = [1, 2, 3, 4, 5]
    print(li1[3] / 2)

finally:
    print("Always executed")

print("Line 3")
print("End")



# ------ program 14---------

try:
    print("open file")
    print("read/write/append",10/0)

except Exception as e:
    print(20/0)

finally:
    print("close file")

#custom exception

#part1
absent = 0
if absent >6:
    print("Terminated")

else:
    print("You can continue with training")