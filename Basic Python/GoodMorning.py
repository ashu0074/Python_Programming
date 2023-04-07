"""
import time 
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
hr = time.strftime("%H")
print(hr)
mn = time.strftime("%M")
print(mn)
sec = time.strftime("%S")
print(sec)
"""
# Python Program to greet them  on the bases of time:-
import time
timestamp = time.strftime("%H,%M,%S")
hr = int(time.strftime("%H"))
if (hr>6 and hr<12):
    print("Good morning Sir ")
elif (hr>=12 and hr<16):
    print("Good Afternoon")
elif(hr>=16 and hr < 20):
    print("Good Evening")
else:
    print("Good night")