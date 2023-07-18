""" 1) tuple =() / Dictionary {key:value}, / set {unique value}"""


#-> if tuple is created so there is no updatation , no insertion and no remove or pop
""" 
* Tuple are faster than list
* Tuple are not mutable
* Method ----> count, index, len, slicing

"""

def func(int1, int2):
    add = int1 + int2
    mutiply = int1 * int2
    return add, mutiply

print(func(2,3))          # in this case o/p is return in form of tuple

add,multiply = func(2,5)   # in this case we have to store the value in different variable
print(add)
print(multiply)


# tuple using range

num = tuple(range(1,11))
print(num)


##########################################################################

""" 2) Dictionary {key:value}"""

user = {'name':'Harshit',"age": 24}
print(user)
print(type(user))

print(user['name'])  # key is used to access the value
print(user['age'])

#1) another way to create dict

user1 = dict(name = 'ashish', age = 24)
print(user1,type(user1))


user_info = {
    'name':'Ashish',
    'age':24,
    'fav_movie': [],
    'fav_tunes': []
}
user_info['fav_movie'].append('Harry Potter')   # acces and data in list inside dict 
print(user_info)

""" 2) add element in the dict """

user_info1 = {}
user_info1['name'] = 'umang'
print(user_info1)

# 2) looping and add keyword in the dictionary
""" a)  In """
print('name' in user_info1) # for key

print("Ashsih" in user_info1.values())   # to check for the values 

""" b)  loop """
for i in user_info:   # for key  values
    print(i)

print("User keys values ")
for i in user_info.values():   # for values
    print(i)

""" c) item method 

it return the list which contain many tuple and each tuple has [(key,values),(key,values)]"""


for i in user_info.items():
    print(i)

for key,values in user_info.items():
    print(f"keys is {key} and values is {values}")



# 3) "add" and "delete" data from dictionary 

user_info1['fav_songs'] = ['songs1','songs2']
print(user_info1)

""" Delete : Pop method ----> pop method delete the values and return it """

poped = user_info1.pop('fav_songs')  # pop return a value
print(f"pop iteam is : {poped}")                          
print(user_info1)

""" 'popitem method': randomley koi key value pair delete kerna h """

poped_item = user_info.popitem()
print(poped_item)

print(user_info)

""" Update:"""

more_info = {'name':'Ashish singh', 'State':"Rajasthan","city":"Udaipur"}  
# in this case "update" is used to update previous dict and add a new data 

user_info.update(more_info)
print(user_info)


# 4  Fromkeys

"""d = {'name': 'unknown', 'age':'unknown',} """

d = dict.fromkeys(['name','age','height'],'unknown')
print(d)

""" when string is pass --> then it took seperate indivisual string in dictionary"""

c = dict.fromkeys("abc", "unknown") 
print(c)

""" Range function --> """

e = dict.fromkeys(range(1,11),'unknown')
print(e)

""" values must be list so :- """

f = dict.fromkeys(['age','name'],['unknown','unknown'])
print(f)


# 5) get --> is used to prevent from error mistak 
print(f['name']) 
print(f.get('Occupation'))   # occupation is not available in key so it's reflect any error--None



""" replacement of "in"  """

if d.get('name'):          # if 'name' in d:
    print('present')
else:
    print('not present')

""" if None ---> False, else----> True"""

# get() method extra

user = {'name':'ashish','age':24}
print(user.get('names','not found'))  # when statement is false then it print "not found!"

# 6) Clear --> clear the dict

c.clear()
print(c)

# 7) copy()

d1 = d.copy()
print(d1)

""" d1 =d  vs d1 = d.copy()
in * d1 =d --> in this case it share the memory location 
* d1 = d.copy()---> in case new memory is created """


#######################################################

""" 3) Sets """

"""set --{} unique value store """

#1) add

s = {1,2,4,2,5,3,5,6,4}
print(s)

s.add(9)
print(s)

# 2) remove 

s.remove(3)
print(s)

""" s.remove(7)       it give key error """

s.discard(7)   # it not show any error
print(s)

# 4) copy
s1 = s.copy()
print(s1)

#3) clear

s.clear()
print(s)


print(f"The copy s1 when s is clear : {s1}")


# note 
"""
* In set we not store any list and distionary and tuple
* Union         s1 | s2
* Intersection  s1 & s2
""" 