"""  17.Write a program that will take three digits from the user and add the square of each digit. """

def square_each(number):
    i = 0
    sum = 0
    while(i<= len(str(number))+1):
        square = number%10
        sum = (square)**2 + sum
        number //=10
        i +=1

    print("The square of each digit : ", sum)

num = int(input("Enter the number :- "))
square_each(num)
