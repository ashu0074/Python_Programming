""" String """
#1. string concatenation 

first_name = 'Ashish'
second_name = 'Singh'
print(first_name + " " + second_name)


#2. input ---> It's always take in form of string

"""
a = input("how much old are you  : ")
print(type(a))

name = input("Enter your name : ")
print("Good Morning"+ " " +  name + " Your age is " + a)
"""
# more than 1 input in single line
"""
name, age = input("Enter the name and age ").split()  # in case --[ ashish 24 ] space must be inserted so it can 
name1, age1 = input("Enter the name and age").split(",")
print(name1)
print(age1)
print(name)
print(age)
"""
# 3) int function 

"""
a = int(input("enter num1 : "))
b = int(input("enter num2 : "))
print(a+b)
"""
###########
# 4) Variable
name, age = "Ashish",24
print(age)

x=y=z=1
print(x+y+z)


# 5) String Formating

"""python 3"""

print("hello my name is {}, and my age is {}".format(name, age))

""" python 3.6"""

print(f"hello my name is {name} and my age is {age}")



# 6) String Indexing:-
lang = "Python"
print(lang[2])
print(lang[-1])
print(lang[:3])
print(lang[4:])
print(lang[-1::-1])
print("hello")
print(lang[-1:-4]) # not printed it required to instruct the forward or backward "step  argument " 

print("Ashsih"[::2])



# 7) String Method 

""" 
Function -->len(),
Method --> lower(), upper(), title(), count()
"""
print(len("Harshit"))  # only for string character 
# print(len(123))

name = "AsHish"
print("Lower: ",name.lower())
print("Upper : ",name.upper())
print("Title : ", name.title())
print("count h : ", name.count("h"))  # Count is case sensetive


# 8) Strip method -- 
"""is used to remove the space in b/w word
* lstrip() - for left space remove
* rstrip() - for right space remove
"""

str1 = "      Ashish      "
str2 = " ............ "
print(str1 + str2)
print(str1.lstrip()+ str2)
print(str1.rstrip()+str2)
"Strip"
print(str1.strip()+ str2)
str3 = "Ashish singh"
print(str3.strip())


# 9) Find and Replace and Center
""" Replace """
string = "hello it's revision time "
print(string.replace(" ","_"))

new_string = "this is my new string and it is very useful for replace method "
print(new_string.replace(" is"," was",3))

""" Find """
print(new_string.find("is"))
pos1 = new_string.find(" is")  # if we want to find the next is location so we can start string from 5 
print(type(pos1))
print(new_string.find(" is",pos1 + 1))

""" Center ---> *ashish* """
name = 'ashish'
print(name.center(8,"*")) 
print(name.center(10,'*'))

name_len = input("enter the name of user : ")
print(name_len.center(len(name_len) + 4,"*"))


""" # string are 'Imutable' 
* Replace() method not change the orignal string
"""

 