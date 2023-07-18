# 1) if statement
age = int(input("Enter the age: "))
if age >= 18:
    #pass
    print("you are eligible to watch movie")
else:
    print("soory, you are not able to watch movie")



# 2) check the "empty string"

name  = input("Enter the name : ")

if name:                             # true if string is not empty
    print(f"your name is {name}")
else:
    print("you didn\'t type anything ")


#3) While loop 
"""
i = 1
while i<=10:
    print(f"hello world {i}")
    i += 1
"""

""" Sum of number form 1 to 10 """
i = 1
sum = 0 
while (i<=10):
    sum += i 
    i += 1  

print(sum)


# 4) infinte loop
"""
while True:
    print("This run infinite time becoz bool value == True")
"""

#5) For loop --- range function 

for i in range(5):
    print(f"For loop : {i}")


""" Sum from 1 to 10 using for loop """

total = 0
for i in range (1, 11):
    total += i
print(f"Total : {total}")


""" User input for  no.of sum """
total = 0
num = int(input("Enter the number : "))
for i in range(1, num+1):
    total +=i

print(f"Total : {total}")


# 6) Break and Continuue

for i in range(1,11):
    print(i)
    if i == 5:
        break

""" Continue :-  Used to skip any number """
for i in range(1,11):
    if i ==5:
        continue
    print(i)

""" For loop and string """
name = "Harshit"
for i in name:
    print(i)