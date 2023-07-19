""" Inheritance and Dunder"""

class Phone:  # base class / Parent clas
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    def make_a_call(self,number):
        return f"calling {number}........"
    


# Now making the child class 

class Smartphone(Phone):
    def __init__(self, brand, model_name, price,ram, internal_memory, rear_camera):
        """ two method to inherite the attribute from previous class --1) uncomman way 2) super meth
        1) uncoman way -- include the self 
        # Phone.__init__(self,brand,model_name, price)
        """
        super().__init__(brand, model_name, price)  # super().__init__
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = rear_camera

# 2 class inherite from single parent class
class Smartphone2(Phone):
    def __init__(self, brand, model_name, price,ram, internal_memory, rear_camera):
        """ two method to inherite the attribute from previous class --1) uncomman way 2) super meth
        1) uncoman way -- include the self 
        # Phone.__init__(self,brand,model_name, price)
        """
        super().__init__(brand, model_name, price)  # super().__init__
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = rear_camera

######################################################################
"""3) Multilevel Inheritance:-"""

class Flagship(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, frontcamera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.frontcamera = frontcamera

        """ Method Overriding """
    def full_name(self):
        return f"{self.brand} {self.model_name} {self._price} method overriding"

phone = Phone("Nokia","1010",5000)
smartphone = Smartphone('onepuls','node2',25000,8,128,64)
smp2 = Smartphone2('Pixel','6a',35000,6,128,50)
print(phone.full_name())
print(smartphone.full_name()+f" and price is {smartphone._price}")

""" 2 class inherite from single Parent class"""
print(smp2.full_name())

""" 3 Multiple Inheritance"""
flagph = Flagship('Pixel','7a',45000,8,128,50,12)

print(flagph.full_name())

#4 Method Resolution Order
""" it is used to find the function available in the particular class or not and find in the order wise.

print(help(Smartphone2))
print(help(Flagship))
"""

#5 isinstance() and issubclass()
""" 1) isinstance()-- is used to check weather this "object" belong to that class or not
2) issubclass() -- is used to check whather this class is subclass  """
print(isinstance(flagph,Smartphone))  # true because due to inheritance 
print(issubclass(Smartphone,Phone))
print(issubclass(Phone, Smartphone ))  # Phone is not subclass it parent class


####################################################

# 6) Multiple Inheritace
""" Note
Python Programer avoid the "Multiple Inhertance" """


######################################################3

#7) Magic/dunder method
""" Dunder method --> __any__ it special magic method """

l = [1,2,3]
print(l)


class Cellphone:  # base class / Parent clas
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def phone_name(self):
        return f"{self.brand} {self.model}"
    
    # str and repr

    def __str__(self) :
            return f'{self.model_name} {self._price}'


    def __repr__(self):
            return f'{self.model_name} model of my_phone obect'
    
    # we can generally create our own function 
    
    def __hight__(self):
         return  len(self.brand)      # call--- print(my_phone.__hight__())




my_phone = Cellphone('nokia','asha1100',1000)
print(my_phone)    # in this it give us the address of this 

""" for this if want to print element directley so we can do 

dunder 2 type:- ---- 
1)str
2)repr -- representation (jab hme kuch print kerana ho )

* when str and repr both function call by object only ---> then str run repr not


$$$$$$$$$$$$ Note:-

str- Nicely Formated string
repr- Is used to write Python code -- used to return an object

"""

print(repr(my_phone))   # In thish case we run the repr 

# calling our own special function 

print(my_phone.__hight__())



######################################################
""" Operator overloading  """

class Cellphone:  # base class / Parent clas
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    def __add__(self,other):
        return self._price + other._price
    
    def __mul__(self,other):
        return self._price * other._price

    # in this if we want to add the 2 object value so we create spectial "operation overloading"


phone1 = Cellphone('nokia','asha1100',1000)
phone2 = Cellphone('nokia','1600',1250)
print(phone1 + phone2)   # in this + is used to call __add__ so we can do overload this operator
print(phone1 * phone2)

####################################################3

""" polymorphism

many_form-- kisi bhi cheez ki ek se jada form hona

eg- + is used to add 2 no. as well as it used to concat two string  
* len is used to calculate the len of list, tuple,string etc  """


