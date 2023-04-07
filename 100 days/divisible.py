""" 13.Write  a program that will tell whether the given number is divisible by 3 & 6."""
# 3 divisible -- sum of all digit and divide by 3
# 6 divisible -- divisible by 3 and 2

def divisible_6(number):
    value = number
    i = 0
    sum = 0
    while (i <= len(str(number))+1):
        sum = sum + (number % 10)
        number //= 10
        i +=1
    if (sum %3 == 0) and (value %2 == 0 ):
        print(" {} is divible by 6 ".format(value))
    else:
        print("{} Not Divisible by 6".format(value))


num = int(input("Ente the no: - "))
divisible_6(num)
