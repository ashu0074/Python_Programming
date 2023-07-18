""" Decorator ---@ shortcut"""
def square(a):
    return (a**2)

# In case "s = square" now s is point to square and they share the same memory location 
s = square

print(square)
print(s)


# 2. Pass a function as argument

l = [1,2,3]

def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    
    return new_list

def my_map2 (func,l):
    return[func(i) for i in l]

"""print(my_map(square,l))"""
print(my_map(lambda a:a**2,l))
print(my_map2(lambda x:x**3,l))


# 3) Function returning Function ---" closures"/ "First class function "

def outer_fun(msg):
    def inner_fun():
        print(f"Inside the inner func:-{msg}")
    
    return inner_fun

var = outer_fun("Function return Functin ")

""" In this case "inner fun" and "outer fun" has same """
var()


################################################################33


""" Decorators - enhance the functionality of other function """

def fun1():
    print("this is function 1")

def fun2():
    print("This is function 2")

""" decorator is used to enchance the functionality of the fun
* let print this is awesome without change in the fun
"""

def decorator_function(any_function):
    def wrapper_fun():
        print("This is awesome function ")
        any_function()
    return wrapper_fun

var = decorator_function(fun1)
var()

var1 = decorator_function(fun2)
var1()

# shortcut

@decorator_function
def fun3():
    print("This is @decorator function shortcut ")
fun3()



# Overcome from drawback

def decorator_function1(any_function):
    def wrapper_fun(*args,**kwargs):
        print("This is awesome function ")
        any_function(*args,**kwargs)
    return wrapper_fun


@decorator_function1
def fun4(a):
    print(f"This is function with argument {a} ")


fun4(8)



# return in th function 

def decorator_function2(any_function):
    def wrapper_fun(*args,**kwargs):
        print("This is awesome function ")
        return any_function(*args,**kwargs)   # for this we must return in the funciton 
    return wrapper_fun

@decorator_function2
def add(a,b):
    return a+b

print(add(4,5))


##########################################33

""" For docstring"""

from functools import wraps
def decorator_function4(any_function):
    @wraps(any_function)
    def wrapper_fun(*args,**kwargs):
        """ this is wraper function """
        print("This is awesome function ")
        return any_function(*args,**kwargs)   # for this we must return in the funciton 
    return wrapper_fun


@decorator_function4
def add(a,b):
    """ this is add function """
    return a+b

print(add.__doc__)
print(add.__name__)



###################################3

""" Decorators as argument  ---nested decorators function """

