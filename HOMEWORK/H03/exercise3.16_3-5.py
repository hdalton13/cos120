#Exercise 6.13 #3-5
#Heather Dalton

import turtle

#3
def drawPoly(someturtle, somesides, somesize):
    angle=360/numSides
    for reps in range (numSides):
        t.forward(length)
        t.right(angle)
    return

def main3():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    drawPoly(tess, sides, 50)

#4
def exercise4(t):
    for reps in range (20):
        for i in range(4):
            t.forward(100)
            t.right(90)
        t.right(18)

def main4():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    exercise4(tess) 

#5
def exercise5a(t):
    #part 1
    length= 5
    for reps in range(50):
            t.forward(length)
            t.right(90)
            length= length+5

def exercise5b(t):
    #part 1
    length= 5
    angle=91
    for reps in range(50):
            t.forward(length)
            t.right(angle)
            length= length+2
           

def main5():
    wn=turtle.Screen()
    tess= turtle.Turtle()
    tess.color("blue")
    exercise5b(tess) 

        

main5()
