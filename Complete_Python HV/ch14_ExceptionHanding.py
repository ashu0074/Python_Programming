""" Exception Handling 
Try except else finally

Exception -- Error occur during the execution time

"""
while True:
    try:
        age = int(input("Enter the age "))
        
        # seven to generate an error then except condition is run 

    # if we know which type of error is occur 
    except ValueError:
        print("maybe you enter string instead of number , plz try again ")

    # if error != ValueError and other error so we use this --- except
    except:
        print('Invalid Input')

    # else -- block run when there is no exception occur's
    else:
        if age < 18:
            print("you can't play this game")
        else:
            print("you can play this game")

        break
    finally:
        print("This will run either error occur or not ")

# if except condition is run then "age" variable is not form 


""" Try except else finally """

def divion(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print("You divide the number with zero ")
        print(err)                                       # print default msg

    except NameError:
        print("You may enter the wrong attribute entry : ")
    except TypeError:
        print("Number must be int or float")

    except:
        print("Unexpected Error")
    
        
print(divion(4,'a'))
        