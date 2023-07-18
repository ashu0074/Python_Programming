# 30.2
""" no of time count instance used """

class Person:
    count_instances = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instances +=1
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

p1 = Person('Ashish','Singh',24)
p2 = Person('Yogesh','Singh',25)
print(Person.count_instances)


