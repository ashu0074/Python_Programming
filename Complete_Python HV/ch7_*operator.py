""" Make flexible function :- ----> 
*operator
*args ------> tuple
**kwargs ----> dict
"""

def total(*args):
    print(args)         
    print(type(args))  # it can store all the args in single "tuple"


total(1,2,3,4,5,6)


def all_total(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

print(all_total(1,2,3,4,5,6,7,8,9))


# 2) *args with normal Parameter

def multiply_num(num1,*args):
    multi = 1
    print(num1)          # just want to show the allocation of num1 and arg
    print(args)
    for i in args:
        multi  *= i
    return multi

print(multiply_num(2,3,4,2,6))   

# note
""" In fixed Parameter = must pass fixed argument 
but in *arg it may remain 0 argument pass"""

# Args as Argument


def multiply_num2(*args):
    multi = 1
    print(args)
    for i in args:
        multi  *= i
    return multi


nums = [1,2,3,4]  # in this if we want to pass "nums" in the multiply_num function 
print(multiply_num2(nums))


""" so to unrevel it : in list -----> *  """

print(multiply_num2(*nums))  # unpack the nums


##################################################################
""" **kwargs --> double star argument 
@ it take argument as dict """

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun(first_name = 'ashish', last_name = 'singh')


def fun1(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')

fun1(first_name = 'ashish', last_name = 'singh')

# dictionary unpacking

d = {'first_name' : 'ashish', 'last_name' : 'singh'}
fun1(**d)



# Function all type of parameter "Order" 

""" (Parameter > *args> default parameter> **kwargs)"""

def fun(name,*args, last_name = 'unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

fun('harshit',1,2,3, a = 1,b = 2)