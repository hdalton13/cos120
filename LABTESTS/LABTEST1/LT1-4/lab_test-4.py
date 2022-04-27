#heather dalton
#09/26/19  @1:12-paused 1:36 2:00-

import turtle
import random

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


