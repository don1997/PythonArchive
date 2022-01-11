file = open("times.txt", 'r')

with open('times.txt') as f:
    contents = f.read()
   



f.close()


print("DATE\t\t", "START TIME\t", "END TIME\t","HOUR\t","MINUTE\t", "SECOND\n")


print(contents)