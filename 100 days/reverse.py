""" Write a program that will reverse a four digit number.Also it checks whether the reverse is true . """

# In this program we can check first that person is try to put exactley 4 digit no. or not  if number len ==4 then we can reverse it :

number  = int(input("Enter the number : "))
last = 0

def number_length(number):
    # return the length of the number
    return len(str(number))

leng = number_length(number)

def  check_out(number):
    if leng == 4:
        rev_number(number,last)
    else:
        print("The no. length is not equal to 4:")
        print("chelo bhai to bhi result dikha deta hu ")
        rev_number(number,last)

def rev_number (number,last):
    while (number>0):
        last = (last*10)+(number%10)
        number = number //10

    print(last)


check_out(number)


