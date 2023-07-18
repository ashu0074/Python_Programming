""" Generator ----> yield """
# Generator are iterators

""" iterator and iterable
l = [1,2,3] ---> iterable

map(lambda x:x**2,l) ---> iterator
"""
# iterable --> iterator  (we use -- iter and next)

l = [1,2,3]

i = iter(l)
print(next(i))
print(next(i))   # again print next of i


##############################################
""" Create our own Generator 
1) Generator function 
2) generator comprehension
"""

def num(n):
    for i in range(1,n+1):
        yield(i)

print(num(10))   # generator is created 


numbers = num(10)
for num in numbers:
    print(num)

for num in numbers:
    print(num)

# Note:-
""" Generator -- in this case it print single time because Generator erase the previous number
** Ek baar sequence generate hogi or usko kisi variable me store ker diya then vo single time print hogi 
** agar isi ko for loop me run kerege without storing then it print multiple time  

numbers = num(10)

or 
for i in num(10)"""
##################################################3

# 3) Generator Comprehension 

square = (i**2 for i in range(1,11))
print(square)

