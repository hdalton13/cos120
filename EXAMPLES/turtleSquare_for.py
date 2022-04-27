import turtle


def drawSquare(aTurtle,size):  #function definition
    for i in range(4):
        aTurtle.forward(size)
        aTurtle.right(90)
    return

def main():
    wn=turtle.Screen()
    t=turtle.Turtle()
    sue=turtle.Turtle()
    drawSquare(t,50) #function call
    t.up()
    t.forward(100)
    t.down()
    drawSquare(t,50) #function call
    sue.color("red")
    sue.up()
    sue.forward(100)
    sue.down()
    drawSquare(sue,50) #function call

main()
