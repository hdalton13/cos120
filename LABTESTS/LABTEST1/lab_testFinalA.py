#heather dalton
#09/26/19  @12:10-2:55
import turtle
import random

#1
def distance(x,y):
    distance= math.sqrt((x-0)**2+(y-0)**2)
    return distance

print(distance(3,4))
print(distance(5,6))

#2
def wanderTurtle(maxWanderSegments, maxDisntance):
    wn=turtle.Screen()
    bob=turtle.Turtle()
    maxW= random.randrange(0,maxWanderSegments+1)
    for i in range(maxW):
        angle= random.randrange(0,360)
        bob.right(angle)
        distance=random.randrange(0,maxDisntance+1)
        bob.forward(distance)

wanderTurtle(100, 50)

#3
def drawRightTriangleInverted(rows):
    space=""
    for i in range(rows,0,-1):
        print(space+"*"*i,end="")
        print("")
        space=" "+space
    print("")

drawRightTriangleInverted(6)
drawRightTriangleInverted(12)

#4
def drawBisected(size):
    wn=turtle.Screen()
    bob=turtle.Turtle()
    #for i in range(4):
    for i in range(3):
        bob.forward(size)
        bob.right(60)
    bob.right(60)
    bob.forward(size*2)
    bob.left(120)
    for i in range(3):
        bob.forward(size)
        bob.left(60)
    for i in range(2):
        bob.forward(size)
        bob.left(120)
        bob.forward(size*2)
        bob.left(120)
   
drawBisected(100)

#5
def stringProgression(string):
    new=""
    index=1
    for i in range(len(string)):
        if(i==index):
            new= new+ string[i]
            index=index*2
    return new

print(stringProgression("This is a test, this is only a test."))
print(stringProgression("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure."))
