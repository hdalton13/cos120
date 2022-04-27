#heather dalton
#09/26/19  @12:20-12:35

import turtle
import random

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
