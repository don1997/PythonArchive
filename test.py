print("Hello World")
#this is a a comment

print("Input name")
myname  = input()

print("Hello " + myname)

print("what do you want i to be: ")
i = int(input())
if i < 5:
    print("i is less than 5")
else: 
    print("i is greater than 5")

j = 0
while 1:
    print("Cat")
    j = j + 1
    if j == 10: 
        break

#this contains a void function
def Hello():
    #this contains a for loop    
    for x in range(0,5):
        print("Hello" + str(x))
#this is a function call
Hello()

supplies = ['pencil', 'paper', 'cars']

#for i in range(len(supplies)):
 #   print(i)


for index, item in enumerate(supplies):
    print(index)

import random

pets = ['Dog', 'Cat', 'Moose']

print(random.choice(pets))

random.shuffle(pets)
print(pets)

