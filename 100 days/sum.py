""" 4.Write a program that will give you the sum of user input  digits """
# we can store in the list and sum to get proper output
i  = 1
my_list = []
user_input = int(input("Enter the no. of digit : "))
while(i <= user_input):
    number = float(input("enter the no."))
    my_list.append(number)
    i += 1 

total = sum(my_list)
print("The sum {} no. is : {} ".format(user_input,total))
