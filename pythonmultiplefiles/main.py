#tut url: https://www.youtube.com/watch?v=jx4eysaLTrg

from functions import square
from functions import zeroExponent
import useless
###square calc
print("Enter a number to be squared: ")
userIN = int(input())



#calls function and assigns to variable
#note how import library + . to call
#When using from import you no longer have to do
#library + .

answer = square(userIN)
print("\n")

print("The squared number is: " + str(answer))

###zero exponent

print("Enter a number to be zero exponent: ")
userIN = int(input())

answer = zeroExponent(userIN)
print("\n")

print("The zero exponent number is: " + str(answer))

### example for reference whole library


text = useless.uselessFunc()

print(text)




