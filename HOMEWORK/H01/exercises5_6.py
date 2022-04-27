#Exercises 5.6 #16-19
#Heather Dalton

import random
import math

#16
print ("Excercise 5.6 #16")

for x in range(10):
    bob= random.random()
    print(bob)
    print("")


#17
print ("Excercise 5.6 #17")

for x in range(10):
    arandom= random.randrange(25,36)
    print(arandom)
    print("")

#18
#print ("Excercise 5.6 #18")

side1= input("What is your side length")
side2= input("What is your second side length")
hypotenuse= math.hypot(int(side1), int(side2))
print(hypotenuse)
print("")

#19
print ("Excercise 5.6 #19")
pi= 3+(4/(2*3*4)) - (4/(4*5*6))+ (4/(6*7*8))-(4/(8*9*10)) #and it goes on that same pattern forever

g=2
h=3
d=4
for x in range(10000): #just need to make loop longer untill it equals 3.14
    pi_2= 3+ (4/(g*h*d))
    g= g+1
    h= h+1
    d= d+1
    pi_2= pi_2 - (4/(g*h*d))

print("Calculated attempt 1=",pi)
print("Calculated attempt 2=",pi_2)
print("Actual pi=",math.pi)

