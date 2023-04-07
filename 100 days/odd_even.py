""" 6.Write a program that will tell whether the number entered by the user is odd or even."""
number = int(input("Enter the number : "))

def oe(number):
    if number %2==0 :
        print("Even")
    else:
        print("Odd")

oe(number)



