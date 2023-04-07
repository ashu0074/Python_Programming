""" 8.Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not. """
# in case 3 angle and 3 side are to find out the 1st traingle is form and then area of triangle

from odd_even import area_traingle

first = float(input("Enter the 1st Angle: "))
second = float(input("Enter the 2nd Angle: "))
third = float(input("Enter the 3rd Angle: "))

sum = first+second+third


def area_traingle(first,second,third):
    if (first ==90) | (second ==90 )| (third ==90):
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5*base*height
    else:
        print("Enter the 3 dimension of the triangle : ")                   
        fside = float(input("Enter the first side of the triangle : "))         
        sside = float(input("Enter the second side of the triangle: "))         
        tside = float(input("Enter the Third side of the triangle: "))              
        semip = 0.5(fside+sside+tside)
        area = (semip*(semip-fside)*(semip-sside)*(semip-tside))**0.5
    
    return area
    
    
if sum == 180:
    print(" Angle to form triangle: ")
    output = area_traingle(first,second,third)
    print("Area of Triangle is : {}".format(output))

else:
    print("Sorry Angle not form triangle")



