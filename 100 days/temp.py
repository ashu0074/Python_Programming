""" 2.Write a program that will convert celsius value to fahrenheit"""
# F to C ---> Example: (50°F - 32) x .5556 = 10°C
# C to F ----> Example: (30°C x 1.8) + 32 = 86°F’

from old import oldest_one   # In this case we load the "oldest function" form the old.py file and return value store in teh psage and set as default for futher use

psage = oldest_one()   # in this

def cf_fc():
    user_input = input("Enter the Temp In 'Fahrenheit' or 'Celsius' : ").lower()
    if user_input == 'fahrenheit' or 'f':
#        fah = int(input("Enter the Fahrenheit Temp : "))
        celsi = (psage - 32)*0.5556
        print("{} C Temprature".format(celsi))
        return(celsi)

    elif user_input == 'celsius' or 'c':
#        celsi = int(input("Enter the Celsius Temp:  "))
        fah = (psage * 1.8) + 32
        print("{} F Temprature".format(fah))
        return(fah)

    else:
        print("You Enter Wrong Entry : ")
        exit()


cf_fc()


