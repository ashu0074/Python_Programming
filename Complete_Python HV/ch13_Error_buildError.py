""" Build in Error / Exception Handling/ raise your own error/ debugging """

# 1) Error type:-
""" 
* Syntax error :-        "invalid syntax"
* Indentation error:-    ""IndentationError
* name error:-           "name is not define"
* typeError:-            "TypeError: Unsupported operand type(s)"
* IndexEror:-            "IndexError"
* ValueError             "ValueError:- invalid literal "
* AttributeError         "when we used invalid function -- attribute"
* KeyError               "when we search wrong key in dictionary "
"""

###############################################################

#2) Raise Error --raise

def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("OOP's you are passing wrong data type of function")

#print(add('5','7'))

""" Example 1 - raise error
* NotImplementedError
* Abstract mehtod

 """

class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
       # return 'this is animal sound'
        raise NotImplementedError('You must define this method in subclass also')
    
    """ In this case - apne ko ye chaiye jo bhi animal class ko inherite kerega vo sabhi class ko "sound" function create kerna hoga"""
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'bhow bhow'

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meao meao'

doggy = Dog('boony','pug')
print(doggy.sound())

#3) Example 2)

class Mobile:
    def __init__(self, name): 
        self.name = name

class Mobilestore:
    def __init__(self):
        self.mobile = []

    def add_mobile(self,new_mobile):

        """ In this case we want to add only Mobile class  """
        if  isinstance(new_mobile, Mobile):
            self.mobile.append(new_mobile)
        else:                                       # raise an error
            raise TypeError('new mobile should be object of mobile class ')



oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s8'
mobostore = Mobilestore()
print(mobostore.mobile)    # initallt empty now we can append

mobostore.add_mobile(oneplus)
print(mobostore.mobile)
mobo_phone = mobostore.mobile
print(mobo_phone[0].name)
# mobostore.add_mobile(samsung)   # this throw the raise error 
# print(mobostore.mobile)



