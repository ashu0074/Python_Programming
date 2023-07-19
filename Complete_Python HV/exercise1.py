#1) input with string formating

num1,num2,num3 = input("Enter the number 3 number with comma seperated : ").split(",")
avg = (int(num1)+int(num2)+int(num3))/3
print(f"the avg of {num1},{num2}, and {num3} is {avg}")


#2  
# ask user name and print back user name in reverse order  &
# try to make your program in 2 lines using string formatting

name = input("Enter the name ")
print(f'reverse order name {name[::-1]}')


#3)

# take 2 comma seperate input 1st is name and 2 nd is character then
# in o/p it reflect the user  name length and count the character that user inputed
name , word = input("Enter the name, character : ").split(",")
print(f'the length of the string is {len(name.strip())}, the no. of occurance of word {word}:{name.strip().lower().count(word.strip().lower())}')



#4)
""" Gussesing the game """

import random
random_num = random.randint(0,9)
print(random_num)
num = int(input("Enter the number : "))
if (num != random_num):
    print("sorry")
    if (num >random_num):
        print("Number is greater than random number")
    else:
        print("Number is lower than random number ")
else:
    print("You won ")


# 5
""" Enter the age of the person and age if name inital character is started with -- "a" /"A" and age >10 
then we he is eligible to watch the movie "coco" movie """

name = input("Enter the name : \n")
age = int(input("Enter the age : "))
updated_one = name.lower()
if (updated_one[0] == 'a') and (age > 10):   # if age >=10 and (name[0] == 'a' or name[0] =='A')

    print("Congratulation you able to watch movie ")
else:
    print("Sorry")


# 5)
""" Sum of n no. of natural number """

num = int(input("Enter the number : "))
i = 1
sum = 0

while (i <=  num):
    sum += i
    i += 1 
print(f"Sum : {sum}")

    

 
# 6)
""" ask user to input a number containing more than one digit  
eg -123 ....  calculate 1+2+3"""


num = input("Enter the Number : ")
i = 0
sum = 0

while(i < len(num)):
    sum += int(num[i])
    i += 1
print(f"Sum {sum}")

""" Using For loop : """
sum = 0
num = input("Enter the number : ")
for i in range (0,len(num)):
    sum += int(num[i])

print(f"Sum of {num} : {sum}")


# $$$
#7 
""" Ask the user for name  and print count of each words """

name = input("Enter the Name : ")

temp_var = ""  # in this we can create the temp variable which store the previous word and we use to compare it 
i = 0
while (i<len(name)):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")

    i += 1 


""" For loop """

temp_vari = ""
user_inp = input("Enter the string : ")
for i in range (0,len(user_inp)):
    if user_inp[i] not in temp_vari:
        temp_vari += user_inp[i]
        # print(temp_vari)
        print(f"{user_inp[i]}: {user_inp.count(user_inp[i])}")



#8
""" Modify the number guessing game : - using random number  """
import random
random_num = random.randint(0,100)
print(random_num)
guess = 1
num1 = int(input("Enter the number b/w 0 to 100 : "))
game_over = False

while not game_over:
    if num1 == random_num:
        print(f"you win, and you guessed this number in {guess} times ")
        game_over = True

    else:
        if num1 > random_num:
            print("too high")
            guess += 1
            num1 = int(input("Enter the number again: ")) 
        elif num1< random_num:
            print("too low")
            guess += 1
            num1 = int(input("Enter the number again : "))


# ****** Dry Principle *******
import random
random_num = random.randint(0,100)
print(random_num)
guess = 1
num1 = int(input("Enter the number b/w 0 to 100 : "))
game_over = False

while True:
    num1 = int(input("Enter the number b/w 0 to 100 : "))
    if num1 == random_num:
        print(f"you win, and you guessed this number in {guess} times ")
        break

    else:
        if num1 > random_num:
            print("too high")
        elif num1< random_num:
            print("too low")

         # DRY Principle :- Don't repeat yourself   
        guess += 1
        continue




#9)
""" define a funciton which tell which no. is greater among 3 """

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


#10)
""" Palindrome """
def is_palindrome(arg):
    if arg == arg[::-1]:
        return "True"
    return "False"  

# print(is_palindrome("madam"))

op = is_palindrome("madam")
print(op)

"""    def is_palindrom(word):                    # in this case either it return True and False and we print it
            return word == word[::-1]_
 """


 #11)
 #  """ Fibonacci series """

# 0 1 1 2 3 5 8 12 21 34

def fibonacci_seq(n):
    a = 0  # first number
    b = 1  # second number

    if n ==1:
        print(a)
    elif n==2:
        print(b)
    else:
        print(a,b,end = " ")
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            print(b, end = " ")


fibonacci_seq(5)

# 12) Square of lst variable using function 

def square_list(l):
    sqrt_ls = []
    for i in l:
        sqrt_ls.append(i**2)
    return sqrt_ls

print(square_list([1,2,3,4]))
number = list(range(1,11))
print(square_list(number))

# 13) 
"""will return a reversed list --- without using "reverse method" and "[::-1]", try pop and append method """
""" Using ---l.reverse() or return l [::-1]
"""

def rev_lst(l):
    new_lst = []
    for i in range(len(l)):
        a = l.pop()   # pop always return a value
        new_lst.append(a)
    return new_lst

print(rev_lst([1,2,3,4]))


# 14)  
"""return list with reverse of every element in that list
eg - [['abc'],['tuv']]--->[['cba'],['vut']] """


def revlst(l):
    new_lst = []
    for ele in l:        # in this case list of list -- that main reason to run nested loop 
        for i in ele:
            new_lst.append(i[::-1])
    return new_lst


print(revlst([['abc'],['tuv']]))




# 15) 
"""filter odd and even :-
eg - list --[1,2,3,4,5,6,7,8,9]
o/p --> [[1,3,5,7,9],[2,4,6]] """

def filter_oe(l):
    evenls = []
    oddls = []
    for i in l:
        if i%2 ==0:
            evenls.append(i)
        else:
            oddls.append(i)
        
    output = [oddls , evenls]
    return output


number = list(range(1,11))
print(filter_oe(number))


# 16)
""" function as input take 2 list and return single list with comman element in it 
input -> [1,2,3,4],[1,2,7,6]-----> output [1,2]"""


def comman_ele(l1,l2):
    comman = []
    for i in l2:
        if (i in l2) and (i in l1):
                comman.append(i)
    return comman


print(comman_ele([1,2,3,4],[1,2,5,6,4]))

#17) 
""" Function  [1,2,3,[1,2],[3,4]] as input  --> o/p as no.of list inside list  """

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count +=  1
    return count
    
mixed = [1,2,3,[1,2],[3,4]]
print(sublist_counter(mixed))


# 18)

""" Function take an argument as n input --> in this it return in form of dict --> {1:1,2:8,3:27}"""


def dictcube (n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube

print(dictcube(5))


# 19
""" word counter dictionary  """

# note --- Dictionary has espical thing that he never repeate the key it always overlaps with previous one

def word_counter(s):
    count = {}
    for char in s :
        count[char] = s.count(char)

    return count

print(word_counter('AshIsh SingH'))


# 20
""" User se data input kerana or usko apni string me insert kerna h """


user = {}

name = input("Enter the name of the user: ")
age = input("Enter the age of the user : ")
fav_movies = input("your fav movies seprated by , ").split(",")  # split list convert and join -- str convertor
fav_songs = input("Enter fav songs seperate by , ").split(",")


user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

# print(user)

""" If we want to print the in order form """

for key,values in user.items():
    print(f"{key}:{values}")



# 21) 
""" Using list comprehension print reverse string in list:-
l = ['abc','tuv','xyz']---->['cba','vut','zyx']"""

l = ['abc','tuv','xyz']

rev_lst = [i[::-1] for i in l]
print(rev_lst)

""" using function """

# def reverse_string(l):
#     return [i[::-1] for i in l]



# 22)
""" num to string define a function 
input --> [True,false, [1,2,3],1,1.0,3]
output ---> ['1','1.0','3']"""


def int_float(l):
    return[ i for i in l if (type(i)== int) or (type(i))==float]

lst = [True,False, [1,2,3],1,1.0,3]
print(int_float(lst))




# 23)

def to_power(num1, *args):
    if args:
        return [i**num1 for i in args]
    else:
        return "You didn't  pass any args"

nums = [3,2,4]
print(to_power(2,*nums))


""" How list khali h ki nahi 

l = [1,2]
 
if l:
    print("not empty") --- True
else:
    print("empty") --- False
    """


#24

""" in this case if str "reverse_str" = True --- then
print the list with reverse and 1st title is capital """


def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:          # get function is used to get the key
        return[name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]


names = ['harshit', 'mohit']
print(func(names))

names1 = ['harshit','mohit','rohit']
print(func(names1 , reverse_str = True))    # **kwargs -- reverse_str



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


# 26) 
""" all any function used --- in the input """

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float)for arg in args]):
        total = 0
        for num in args:
            total += num

        return total
    else:
        return "wrong input"
    
print(my_sum(1,2,3,4,5.5,"hello",['harshit']))
print(my_sum(1,5,6,9,8,7,2.5,3.6))


# 27)  Function return Function (closure) practice 

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

cube = to_power(3)
print(cube(5))

square = to_power(2)
print(square(6))


#28 Decorator

from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper_fun(*args,**kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_fun

@print_function_data
def add(a,b):
    """ This funciton take two number as argument and return their sum """
    return a+b

print(add(4,5))


# 28.1
""" Time difference using decorator"""

import time
from functools import wraps

def calculate_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        returned_value = function(*args,**kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f'this funciton took {total_time} seconds')
        return returned_value
    return wrapper


@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)

#28.2

# 28.2

""" Create the decorator which take argument as int or koi bhi data type nahi le """

from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_type = []
        for arg in args:
            data_type.append(type(arg)==int)

        if all(data_type):
            return function(*args, **kwargs)
        else:
            return("Invalid argument")

    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_all(1,2,3,4,5,[4,5.6]))
print(add_all(1,2,3,4,5,6))


# short the code

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(arg)== int for arg in args]):
            return function(*args,**kwargs)
        print('Invalid arguments')

    return wrapper



# 29 
""" Generator"""

def even_generator(n):
    even_lst = [i for i in range(1,n+1) if i%2==0]
    yield(even_lst)


#lst = even_generator(7)

for num in even_generator(7):
    print(num)



#30   OOPS
 
class Laptop:
    discount = 10
    def __init__(self, brand, model_name, price):
        self.brand_name = brand
        self.model_name = model_name
        self.price =price
        self.full_name = brand +" "+model_name

    def apply_discount(self):
        return (self.price)- ((self.price* self.discount)/100)    # Laptop.discout is fix -- class variable
    


l1 = Laptop("hp",'Pavilion',45000)
l2 = Laptop('hp','Gaming series',70000)

print(l2.full_name)
print(l2.apply_discount())
print(l1.__dict__)             # it give or show all the information 

# task if we want to run a discount offer l2 -- 30% seperately then 


l2.discount = 30
print(l2.__dict__)
print(l2.apply_discount())


# 30.2
""" no of time count instance used """

class Person:
    count_instances = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instances +=1
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('Ashish','Singh',24)
p2 = Person('Yogesh','Singh',25)
print(Person.count_instances)


# 31
""" Try except else finally """

def divion(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print("You divide the number with zero ")
        print(err)                                       # print default msg

    except NameError:
        print("You may enter the wrong attribute entry : ")
    except TypeError:
        print("Number must be int or float")

    except:
        print("Unexpected Error")
    
        
print(divion(4,'a'))
        

#32 Files
""" read a data from file2.txt file and then print output in :-
Harshit's salary is 100
Mohit's salary is 50
"""

with open('file1.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}'s salary is {salary}") 

