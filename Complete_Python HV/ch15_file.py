""" File I/O """
# 1) read text file
""" * readfile
* open function      --> open the file read function -- take an argument
* read method        --> read the entire file  
* seek method        --> move the current cursor to that position 
* tell method        --> tell us what is position of our current cursor
* readline method    -> read single line 
* readlines method   --> read multiple line using "slicing"(in this case it store in the list)
* close method       ---> close the file 

"""


f = open('file.txt','r')   # open the file and store in the f object
print(f.tell())
print(f.readline(),end='')
print(f.readline(),end='')
print(f.tell())
print(f.readlines()[:2],end='')
print(f.tell())
print(f.read())

f.seek(0)

# print(f.read()) ---> file data not print again becoz -- cursor position is in last

""" Data distriptor -- closed, name """
print(f.name)
print(f.closed)
f.close()


""" Using Block """

with open('file.txt') as f:
    data = f.read()         # in this there is no need to close it automatically close
    print(data)

print(f.closed)



###########################################################################
#2) Write to file :-
""" w, a, r+ mode 
*w - > w mode is used to overwrite in the file it "delete" previous one make new one entry
*a -> a mode is used to write in file from next to the previous one no previous data is delete
*r+ -> is used to "read and write both  && r+ mode not create the file  " 

** w and a mode both create file if it not present 
"""


with open('file.txt','a')as f:    
    f.write('\please do it ')


# f.seek(len(f.read())) --> first read the entire file collect the length and then put the value in the seek so our cursor move there



##################################################################

#3) Read and Write 
""" ek file ko read kerna h or kisi or file me write kerna h """

with open('file.txt','r') as rf:
    with open ('file1.txt','w') as wf:
        wf.write(rf.readline())    





