#URL: https://www.youtube.com/watch?v=7sFXkJvQ7Qs
#############WRITE TO FILE

#generates text file named input 
open("input.txt", "a")
file = open("input.txt", "w")
#writest to file

file.write("Are you My Mother   72\n")

file.write("The Digging-est Dog   72\n")

file.close()

#################READING FILE
file = open('input.txt', 'r')
data = file.read().split('\n')
#close file after getting data
#can still work with data even after closed
file.close()

print(data)








