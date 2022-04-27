#Exercise 6.13 #8-10
#Heather Dalton

import turtle
import math

#8
def areaOfCircle(radius):
    area= math.pi*(radius**2)
    return area

def main8():
    print(areaOfCircle(3))
#main8()


#9
def drawStar(t, numSides, somesize):
    #angle=360/numSides
    for reps in range (numSides):
        t.forward(somesize)
        t.right(216)
        t.forward(somesize)
    return
def main9():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    drawStar(tess, 5, 100)
#main9()

#10
def main10():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    for reps in range (5):
        drawStar(tess, 5, 50)
        tess.up()
        tess.forward(350)
        tess.right(144)
        tess.down()
main10()
