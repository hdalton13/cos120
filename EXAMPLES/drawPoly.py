import turtle

def drawPoly(t,numSides, length):
    angle=360/numSides
    for reps in range (numSides):
        t.forward(length)
        t.right(angle)
    return

def mainTestPolyDraw():
    wn=turtle.Screen()
    sue= turtle.Turtle()
    #drawPoly(sue, 3, 30)
    for sides in range (3,11):
        drawPoly(sue, sides, 30)
        #sue.rest()

mainTestPolyDraw()
