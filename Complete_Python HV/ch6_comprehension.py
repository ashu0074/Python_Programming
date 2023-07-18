""" 1) List Comprehension :- """

# 1) list of squre from 1 to 10

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)


"""  squares : """
square2 = [i**2 for i in range(1,11)]
print(square2)


# 2) create a list of negative number :-

neg = [-i for i in range(1,11)]    # append kya kerna h or iski range kha se kha jana h 
print(neg)


#3) 
""" names = ['Harshit', 'Ashish', 'Rohit']
create new list and add "inital of name list element" print it"""
names = ['Harshit','Ashish',"Rohit"]

new_list = [i[0] for i in names]
print(new_list)



# 4
""" List Comprehension with if statement : """

numbers = list(range(1,11))
"""
num = []
for i in numbers:
    if i%2 ==0:
        num.append(i)
print(num)
"""


even_lst = [i for i in numbers if i%2==0]
print(even_lst)
""" or """

even_lst2 = [i for i in range(1,11) if i%2==0]
print(even_lst2)

odd_nums = [i for i in range(1,11) if i%2 !=0]
print(odd_nums)



#5 List comprehension with "if-else" statment

"""eg - nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = [-1,4,-3,8,-5,12....]"""

nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = [i*2 if (i %2 ==0) else -i for i in nums]
print(new_lst)


# 6)
""" Nested list Comprehension


example  = [[1,2,3],[1,2,3],[1,2,3]] """

nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)


###############################################################

""" Dictionary Comprehension """

#1)

dict_square = { num :num**2 for num in range(10)}
print(dict_square)

dict_square1 = {print(f"Square of {num}: {num**2}") for num in range(11)}
print(dict_square1)

#2) 
""" Count the no. of character repeate in string"""

s = "Harshit sinGH"
str_count = {i:s.count(i) for i in s}
print(str_count)


#3 )
""" Dict comprehension - IF else
d = {1:'odd',2:'even'}
"""
odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

########################################################

""" Set Comprehension """

s = {i**2 for i in range(1,11)}
print(s)

print(names)
first = {i[0] for i in names}
print(first)