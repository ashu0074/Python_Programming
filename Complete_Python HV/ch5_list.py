""" List """
# 1) aad the iteam in the list ---
"""append"""
fruits = ['grapes', 'apple'] 
fruits.append('mango') 
# fruits.append('mango', 'oragne')    no append multiple iteam in single time 
print(fruits)
fruits.append(['black grapes','lichee'])   # [........[...]] list inside list
print(fruits)


""" 2. insert :- insert used to provide the facility at which position you want to insert any element in list"""

fruits.insert(1,"dragon_fruit")
print(fruits)

""" concatination -- join 2 list """
vegi = ['lady_finger','patato','ginger']
new_lst = vegi + fruits
print(new_lst)

""" 3) extend method """

vegi.extend(['onion','carrot','musterd'])
print(vegi)



# 2) Delete data from list
""" 1) Pop method --> delete the last element"""
vegi.pop()
print(vegi)

vegi.pop(2)
print(vegi)

""" 2) delete ---- del  using the index value """
del vegi[1]
print(vegi)

""" 3) remove --- remove is used to delete the particular element from the lst without indexing """
fruits.remove('dragon_fruit')
print(fruits)


#3) "In" keyword in the list


if 'apple' in fruits:
    print(True)
else:
    print(False)


# 4) Some more method -->
""" 1) Count """
print(fruits.count("apple"))

""" 2. sort() vs sorted()
sort() -- is used to "Permanent" sort
sorted()-- Temporary sort """

numbers = [3,5,1,9,10]

print(sorted(numbers))
print(numbers)
numbers.sort()
print(numbers)

"""3. copy """
numberc = numbers.copy()

print(numberc)

"""4. clear ()"""
numberc.clear()
print(numberc)



#5  ['is' vs '=='  comparision]

fruits1 = ['orange','banana','apple']
fruits2 = ['orange','kiwi','apple']
fruits3 = ['orange','banana','apple']

print(fruits1 == fruits3)
print(fruits1 == fruits2)
print(fruits1 is fruits3)   # is used to compare a object -- both not share same memory location 


#6 split and join

user_input = "Ashish 24"
print(user_input.split())    # split


user_info  = ['ashish','24','1999']  # used to join only string element
print('/'.join(user_info))


# 7 loop in list
fruits1 = ['orange','banana','apple']

for i in fruits1:
    print(i)


# 8 list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1])

""" list inside list to make continues -- nested for loop """

for sublist in  matrix:
    for i in sublist:
        print(i)
 
""" if we want to access 5 in matrix"""
print("access the element in the sublist")
print(matrix[1][1])

print(type(matrix))


#9) More about list--> list with range function , pop method, index, pass list to a function 

""" 1) kisi ko bhi list me convert kerna ho to [list()]-- use ker le"""

numbers = list(range(1,11))
print(numbers)

""" 2) always return the pop element : """

print(numbers.pop())  # always return the pop value
print(numbers)

""" 3) Index method --> used to find the index location of particular value """
print(numbers.index(3))

numbers.append(1)
print(numbers)

print(numbers.index(1, 2)) # index search start from 2nd index value


""" 4)  function with list : """

def negative_no(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_no(numbers))

""" 5) min and max """
min(numbers)
max(numbers)




