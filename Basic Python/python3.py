# loops:
for i in range(3):
    print(i)

print("*"*15)

i = 0
while(i<3):
    print(i)
    i = i+1

x = int(input("Enter the number: "))
while(x>0):
    print(x)
    x-=1
else:
    print("now value come to 0 ")


# do while loop :
secret_word = "python"
counter = 0

while True:
    word = input ("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7:
        break