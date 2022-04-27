#Exercises 6.13 #1 & 2
#Heather Dalton

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()              
wn.bgcolor("lightgreen")


#6.13 #1
def num_one():
    bob = turtle.Turtle()
    bob.color("hot pink")
    bob.pensize(3)
    for i in range(4):
        drawSquare(bob, 20)
        bob.up()
        bob.forward(40)
        bob.down()

#6.13 #2
def num_two():
    fred= turtle.Turtle()
    fred.color("hot pink")
    fred.pensize(3)
    size= 20
    for i in range(5):
        drawSquare(fred, size)
        fred.penup()
        size= size+20
        fred.backward(10)
        fred.right(90)
        fred.forward(10)
        fred.left(90)
        fred.pendown()

#num_one() #6.13 #1
num_two() #6.13 #2













wn.exitonclick()
