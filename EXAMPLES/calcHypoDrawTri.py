import math
import turtle

def calcHypo(a,b):
    hypo=math.sqrt(a**2+b**2)
    return hypo  #actually carry the value back to the place this function was called

def drawTri(t,a,b):
    t.forward(a*20)  #scale it up so we can see it!
    t.left(90)
    t.forward(b*20)
    t.goto(0,0)      #we use this approach rather than calc the angle, etc.

def main():
    side1=3
    side2=4
    c=calcHypo(side1,side2)  #we calc and save the return value
    print("hypotenuse length is",c)
    wn=turtle.Screen()
    sue=turtle.Turtle()
    drawTri(sue,side1,side2)
    #OK - you finish the labels!!!!
    sue.write("a")

main()
