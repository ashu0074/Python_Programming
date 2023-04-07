# 1.User will input (3ages).Find the oldest one
# we try to make in function

def oldest_one():
    first_one = int(input("Enter the age: "))
    second_one = int(input("Enter the age: "))
    third_one = int(input("Enter the age: "))
    if(first_one >second_one) & (second_one>third_one):
        print("First one is older {}".format(first_one))
        return(first_one)
    elif(second_one > first_one) & (first_one >third_one):
        print("Sencond Person is Older {}".format(second_one))
        return(second_one)
    else:
        print("Third Person is Older {}".format(third_one))
        return(third_one)

# psage = oldest_one()          # save the return into new object
# print("the age is ",psage)