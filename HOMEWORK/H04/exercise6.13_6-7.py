#Heather Dalton
#Exercise 6.13 6 & 7

import turtle

#6
def drawPoly(t, numSides, length):
    angle=360/numSides
    for reps in range (numSides):
        t.forward(length)
        t.right(angle)
    return

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)
    
def main1():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    drawEquitriangle(tess,50)

#7
def sumTo(n):
    total=0
    result=(n*(n+1))/2
    return result

def main2():
    t = sumTo(10)
    print("The sum from 1 to 0 is",t)
    


main2()
