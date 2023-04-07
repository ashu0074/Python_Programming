""" 11.Write a program to find the simple interest when the value of principle,rate of interest and time period is given."""

"""  SI Formula 	S.I. = Principal * Rate * Time
     CI Formula 	C.I. = Principal (1 + Rate)Time - Principal
 """

 # P, R , T it require 
princ = float(input("Enter the Principle : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time period : "))

sel = input(" Select 1 for Simple Interest and 2 for  Compund Interest : ")


def simple_intrest(principle, rate, time):
    output = (principle*rate*time)/100
    return output

def compund_intrest(principle, rate, time ):
    output = (principle*(1+(rate/100))**time)-principle
    return output



if (sel == "1") :
    simp = simple_intrest(princ,rate,time)
    print("The SI : {}".format(simp))
   
elif (sel == "2") :
    comp = compund_intrest(princ,rate,time)
    print("the CI : {}".format(comp))
    
else:
    print("You Enter the wrong chooice: ")
    exit()





