a = float(input("Enter the 1s no: "))
b = float(input("Enter the 2nd no. : "))
# a = float(a)
# b = float(b)
s = input("Select the Operator : +,-,*,/,//,%,**  : " )
if(s == "+"):
    print("The addition of a : ", a, "and b : " , b, "is : ", a+b)
elif(s == "-"):
    print("The Substraction of two no. is : ", a-b)
elif(s == "*"):
    print("The Multiplication of two no. is : ", a*b)
elif(s == "/"):
    print("The division of two no is : ", a/b)
elif(s == "//"):
    print("The float division of two no.is : ", a//b)
elif(s =="%"):
    print("The modules of two no. is : ", a%b)
elif(s == "**"):
    print("The exponential of two no. is :",a**b)
else:
    print("You Enter the wrong choice")