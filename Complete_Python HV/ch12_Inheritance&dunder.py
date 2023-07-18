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

