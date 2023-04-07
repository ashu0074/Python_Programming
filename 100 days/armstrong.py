"""  Write a program that will check whether the number is armstrong number or not """

def check(number):
    sum = 0
    i = 0
    ln = len(str(number))
    while (i<= ln+1):
        arm = number %10
        sum = (arm)**ln + sum
        number //=10
    print("output : ",sum)

num = int(input("enter the number "))
check(num)

