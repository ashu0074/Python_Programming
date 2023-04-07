""" 10.Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit """

# in case just ask for the no. of iteam and then store into 2 list one for selling and one for purchase now compare the price


num = int(input("Enter the no. iteam to sell : "))


def cost_compare(num):
    sell_price = []
    cost_price = []
    i = 1
    while(i <=num):
        cprice = float(input("Enter the cost price of {} object : ".format(i)))
        sprice = float(input("Enter the selling Price of {} object: ".format(i)))
        cost_price.append(cprice)
        sell_price.append(sprice)
        i +=1 

    print("Total Cost Price of the Object is : {} Rs".format(sum(cost_price)))
    print("Total Sell price of the Object is: {} Rs".format(sum(sell_price)))

    if (sum(sell_price)-sum(cost_price))>0:
        print("Profit of : {} Rs".format(sum(sell_price)-sum(cost_price)))
    else:
        print("Net Loss of {}Rs".format(sum(sell_price)-sum(cost_price)))



