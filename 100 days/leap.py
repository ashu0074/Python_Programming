""" 7.Write a program that will tell whether the given year is a leap year or not."""

year = int(input("Enter the year : "))

def leap_year(year):
    if (year%4==0) & (year%100!=0) or (year%400==0):
        print("Leap Year")
    else:
        print("Not Leap year")

leap_year(year)