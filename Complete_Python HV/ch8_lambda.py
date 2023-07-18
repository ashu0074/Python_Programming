""" (1) Lambda Expressions (anonymous function )"""

def add(a,b):
    return(a+b)

add2 = lambda a,b : a+b

print(add2(7,4))

# lambda function store variable has no name:-
print(add)
print(add2)


""" even no """

iseven2 = lambda a : a%2 ==0
print(iseven2(6))

""" last char"""

last_char = lambda s:s[-1]

print(last_char("Ashish"))

# lambda ---"if/else"

def func(s):
    if len(s)>5:
        return True
    return False        #else one

""" or """
def func(s):
    return len(s) > 5    # if it right than default it return True and ohterwise it return False

""" Lambda"""
funct = lambda s: True if len(s)>5 else False
print(funct('avc'))



print("*"*25)
#####################################################################

""" (2)  Enumerate() -- for loop

Enumerate is used for position track """

# position track without enumerate

names = ['abc','abcde','xyz']
# 0 --> 'abc' 
# 1 --> 'abcde'

pos = 0
for name in names:
    print(f'{pos}--->{name}')
    pos +=1


# with "Enumerate" Function 
print("With using Enumerate")

for pos,name in enumerate(names):
    print(f"{pos}---->{name}")
    


""" Practice 
* find the position of given string """


def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1

print(find_pos(names, 'ashish'))  # no user
print(find_pos(names, 'xyz'))

###########################################
print("*"*25)

""" (3)  Map Function """

numbers = [1,2,3,45]

def squre(a):
    return a**2

print(map(squre,numbers))
print("we can convert the map object into list/tuple ")

print(list(map(squre,numbers))) # list
print(tuple(map(squre,numbers))) # tuple



# map with lambda

print(" Map function with lambda function ")

squres =  list(map(lambda x: x**2 ,numbers))
print(squres)

# list  comprehension 

squares_new = [i**2 for i in numbers]
print(squares_new)


str1 = ['abc','abcd','abcde']
length = list(map(lambda x: len(x), str1))
print(length)

length1 = map(len, str1)
for i in length1:
    print(i)


print("*"*25)
print("filter function ")
#############################################################

""" (4) filter  (function name, string/list/tuple)"""

def is_even(a):
    return a%2 ==0   

numbers = [3,4,5,2,1,6,9,8,10]

even = tuple(filter(is_even, numbers))
print(even)

""" Using lambda"""

odd = list(filter(lambda x:x %2 !=0 , numbers))
print(odd)


""" List comprehension """

new_odd = [i for i in numbers if i%2!=0]
print(new_odd)


#########################################################

"""(5) iterator vs iterable """

""" list/tuple/ string ---> iterable on we call the iter function on this iterable"""

print(numbers)
number_iter = iter(numbers)
print(next(number_iter))
print(next((number_iter)))

 
##########################################################
""" (6) Zip function """

print("*"*25)
print("Zip Function ")

user_id = ['user1','user2']
names = ['harshita', 'mohit', 'rohit']

print(list(zip(user_id, names)))


""" convert the list of tuple"""
a = [('user1', 'harshita'), ('user2', 'mohit')]
print(dict(a))


# 6.1) Unzip 
print("Zip to unZip")

a = [('user1', 'harshita'), ('user2', 'mohit')]
print(list(zip(*a)))

l1,l2 = list(zip(*a))
print(l1)
print(l2)



l1 = [1,3,8,25]
l2 = [2,4,6,8]
""" find the max from the l1 and l2 print in new list"""

new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)

####################################################################

print("Advanced")

# 25)
"""
average -[1,2,3],[4,5,6],[7,8,9]
 (1+4+7)/3 ,(2,5,8)/3 , (3,6,9)/3  
 """

def average_finder(l1,l2):
    average = [] 
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))

    return average
print(average_finder([1,2,3],[4,5,6]))


""" (*args)----> args = ([],[],[])  
zip(*args)---> unpacked it because *args took in form of tuple """


def average_finder1(*args):
    average = []
    for pair in zip(*args):                   # ([],[],)  unpack zip
        average.append(sum(pair)/len(pair))
    return average

print(average_finder1([1,2,3,4],[2,5,8,7],[5,3,6,4]))




""" Using Lambda Function """

average_lambda =  lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(average_lambda([1,2,3,4],[2,5,8,7],[5,3,6,4]))

###################################################################

print("*"*25)
print("any and all Function ")

number1 = [2,4,6,8]
number2 = [1,2,3,4,5,6,7,8,9]

""" to check the all value True in the list or not """

even1 = []
for num in number1:
    even1.append(num%2 == 0)

print(all(even1))


""" Using List comprehension """
print('all')
print(all([i%2==0 for i in number1]))
print(all([i%2==0 for i in number2]))
print("any")

print(any([i%2 == 0 for i in number2]))

##########################################################

"""7 Advance min() and max() Function """

names = ['Ashish singh','mohit','umang','ab']
print(max(names))

# in this we want to calculate the max on the basis of length

"""def func(iteam):
    return len(iteam)"""

student = [
    {'name':'Harshit','score':90,'age':20},
    {'name':'mohit', 'score':70, 'age':19}
]

print(max(names, key= lambda  item : len(item)))

print(max(student, key = lambda item:item.get('score'))['name'])



""" 8. sorted """

print(sorted(student, key= lambda d:d['age'], reverse= True))


""" 9. Doc string / help """
# eg any function doc string

print(len.__doc__)
print(sum.__doc__)

# help function --> is used to return the sum of any 
# print(help(sum))