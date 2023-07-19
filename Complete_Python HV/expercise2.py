#32 Files exercise
""" read a data from file2.txt file and then print output in :-
Harshit's salary is 100
Mohit's salary is 50
"""

with open('file1.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f"{name}'s salary is {salary}") 

