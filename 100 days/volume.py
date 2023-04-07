""" 12.Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs. """
# 3.14*r**2*h   and volume/1000*40 for the cost 

def cylind_volum(radius,height):
    vol = 3.14*height*(radius)**2
    print("Area of the cylinder : {}".format(vol))
    return vol


def cost(volume,price):
    costing = volume/1000*price
    print("total Costing : {}".format(costing))
    return costing



rad = float(input("Enter the radius of the circle : "))
height = float(input("Enter the height of the circle : "))
price = float(input("Enter the 1 liter cost of milk : "))



volume = cylind_volum(rad,height)
total = cost(volume,price)