""" Function """

def add_two(a,b):
    return a+b 
# print(add_two(5,4))
total = add_two(5,4)   # jab bhi kisi function ko call kero to usko kisi function me store ker lo 
print(total)



# function practice
#1
def lstreturn(arg):
    return arg[-1]

str1 = input("Enter the name : ")
op = lstreturn(str1)
print(op)

#2 
def odev(num1):
    if num1%2 ==0:
        return "Even"
    return "Odd"

a = int(input("Enter the number: "))
print(odev(a))


# 3 shortest way :-

def is_even(num):
    return num%2 ==0    # in this case either it return True or False in boolean


print(is_even(9))

# 4) function without any parameter 
def song():
    return "Happy birthday to you "

print(song())

""" Define a function which tell us which no. i greater : """

def greater(num1,num2):
    if num1>num2:
        return f"{num1} is greater"
    return f"{num2} is greater"

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number "))
op = greater(a,b)
print(op)




def greater1(num1,num2,num3):
    if (num1>num2) & (num2>num3):
        return num1
    elif (num2>num1) & (num1>num3):
        return num2
    return num3

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number "))
c = int(input("Enter the 3rd no. "))
op = greater1(a,b,c)
print(f"{op} is greater")

# 5) (Function inside Function )

"""
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)

print(new_greatest(10,20,30))

"""


# 6) variable Scope

x = 5  # global variable

def func():
    x = 7   # local variable 
    return x

def func1():
    global x  # this statement is used to declare the variable global 
    x = 9   
    return x


print(func())
print(x)

print(func1())
print(x)


#7) Function all type of parameter
