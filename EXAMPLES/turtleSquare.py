import turtle

wn=turtle.Screen()
bob=turtle.Turtle()
sue=turtle.Turtle()
sue.color("red")
sue.forward(100)

def drawSquare(t,size):
    for i in range(4):
        t.forward(size)
        t.right(90)

drawSquare(bob, 75)
drawSquare(sue, 10)
print("That's all Folks!!!")

