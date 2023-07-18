""" OOPS """

class Person:
    def __init__(self,first_name,last_name,age):  # self is object khud
        # instance variable
        print("init method // constructor get called")
        self.person_first_name = first_name
        self.last_name  = last_name
        self.person_age = age


p1 = Person('Mohit','Vashista',24)
p2 = Person('Ashish','Singh',24)

print(p1.person_first_name)
print(p2.person_age)

print("*"*25)

class Laptop:
    def __init__(self,brand, model, price):

        self.brand_name = brand
        self.model_name = model
        self.price = price
        self.laptop_name = brand + ' '+ model   # in this we create a new instance which declare at above

l1 = Laptop("hp",'Pavilion',45000)
l2 = Laptop('hp','Gaming series',70000)

print(l1.brand_name)
print(l2.model_name)
print(l1.laptop_name)

print("/"*25)
####################################################
# 2. OOP instance method

class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above(self):
        # if self.age >18:
        #     return True
        return self.age>18
    

    """ p1 and p2 are the object """

p1 = Person('Ashish','Singh',24)
p2 = Person('Yogesh','Singh',25)

print( p2.full_name())
""" or we can use also this way """
print(Person.full_name(p2))


l= [1,2,3]
# l.clear()     or
list.clear(l)

print(l)

l.append(25)    # or
list.append(l,26)

print(l)


print(p1.is_above())  
#or 

print(Person.is_above(p1))


#############################################
# 3. Class variable
""" jo value hoti h class variable ki vo share hoti her ek object ke sath 
** Fix hoti h 
"""
 
class Circle:
    pi = 3.14    # class variable --- it default
    def __init__(self,radius):
        # instance perameter
        self.radius = radius

    def circumference(self):
        return 2 * Circle.pi* self.radius   # pi value called-- Class.class variable
    

c = Circle(5)
    
print(c.circumference())
    
################################################################
# 4) Class Method ---> Using "Decorator" to declare 

""" 
In "class variable" and "Class object" ---> Calling from 'Class'
In 'instance variable' and 'instance object'--> Calling from 'object'
"""



class Person:
    count_instances = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instances +=1
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    # class Method-- decorator
    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instances} instance of Person class"
    
    # instance Mthod
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1 = Person('Ashish','Singh',24)
p2 = Person('Yogesh','Singh',25)

print(Person.count_instance())      # Classname.classMethod()

# calling the Class Method

###################################################################
#5) Class Method as constructor
""" In this we not call the init method we create our own constructor method """


class Person:
    count_instances = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instances +=1
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    @staticmethod
    def hello():
        return("hello, static method called")

    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first, last, age)



p1 = Person('Ashish','Singh',24)
p2 = Person('Yogesh','Singh',25)  # this is uesd to call the init method
# call the our own Constructor using class method 
p3 = Person.from_string('Harshit,vashith,24')


#6) Static Method 
""" Static Method has no relation with "instance" as well as "class" then we use the static method """

print(Person.hello())


###################################################################

# 7) Encapsulation 


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name

        self._price = max(price,0)
        # if price >0 :
        #     self._price = price
        # else:
        #     self._price = 0

        """
        self.complete_spec = f"{self.brand}{self.model_name} and price {self._price}"  # the price is not update because it depend on __init__
        """

    def full_name(self):
        return f"{self.brand}{self.model_name}"
    
    
    # getter(), setter() ----> used to not change the value use this 
    @property              # getter
    def price(self):
        return self._price
    
    @price.setter                 # is used to set the value
    def price(self,new_price):
        self._price = max(new_price,0)
    

    @property
    def complete_spec(self):
        return f"{self.brand}{self.model_name} and price {self._price}"
    

phone1 = Phone('Nokia','1100',-400)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)

# change the value of price
phone1._price = -500
print(phone1.price)
"""print(phone1.complete_spec())
property attribute ---->     no require to use () during calling """

print(phone1.complete_spec)


