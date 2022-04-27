import turtle
#EXTERNAL DRIVE
def drawSquare(t,length,color):
    t.fillcolor(color)
    t.begin_fill()
    for num in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

def drawRow(t,length,color1,color2):
    for i in range(4):
        drawSquare(t,length,color1)
        t.forward(length)
        drawSquare(t,length,color2)
        t.forward(length)

def drawCircleFilled(t,size,color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size*.5)
    t.end_fill()

def drawChecker(t,wn,row,col,size):
    
    wn.tracer(False)
    t.up()
    t.goto(0,0)
    t.down()
    y=(row*size)
    x=(col*size)+(.5*size)
    t.color("black","green")
    t.fillcolor("green")
    t.up()
    t.goto(x,y)
    t.down()
    drawCircleFilled(t,size,"green")
    t.up()
    t.goto(x,y+.1*size)
    t.down()
    t.circle(.8*size*.5)
    t.up()
    t.goto(x,y+.2*size)
    t.down()
    t.circle(.6*size*.5)
    t.up()
    t.goto(x,y+.3*size)
    t.down()
    t.circle(.4*size*.5)
    t.up()
    t.goto(x,y+.4*size)
    t.down()
    t.circle(.2*size*.5)
    wn.tracer(True)

def drawLabels(t):
    wn=turtle.Screen()
    wn.tracer(False)
    t.up()
    t.color("white")
    y=1
    y1=1
    x1=0
    t.goto(x1,y1)
    
    letters= ['A','C','E','G']
    for ch in letters:
        for col in range(0,8,2):
            t.goto(col+.77,y+0.05)
            t.write(ch+str(col))
    
        x=x1
        x1=x
        y=y1+2
        y1=y
      
    
    x=1
    y=2
    y1=2
    x1=1
    letter=['B','D','F','H']
    for ch in letter:
        for col in range(1,8,2):
            t.goto(x+0.77,y+0.05)
            t.write(ch+str(col))
            x+=2
        x=x1
        x1=x
        y=y1+2
        y1=y
    wn.tracer(True)

    
def checkerboard(length):
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,9,9,-1)
    wn.tracer(False)
    bob=turtle.Turtle()
    bob.hideturtle()    
    c1="gray"
    c2="red"
    for x in range(8):
        drawRow(bob,length,c1,c2)
        bob.backward(8*length)
        bob.left(90)
        bob.forward(length)
        bob.right(90)
        #switch c1 and c2 contents
        temp=c1
        c1=c2
        c2=temp
    drawLabels(bob)
    #drawChecker(bob,wn,0,0,length)
    wn.tracer(True)
        
        
checkerboard(1)







'''3) Write a simple loop that asks the user where they wish to place a checker.
Place a checker there, overwriting the square.  When you ask again and they
give another location, remove the checker from the current location and place
it in the new location,
while restoring the previous location and label.
Use a while loop that continues this process until they type "quit" instead of a
valid location ("A0","A2", etc.).If they enter an invalid location,
e.g. "B0", disallow the move and ask for another location (do this until
they either enter quit or give you a good location).'''

#ask what they want to move and where they want to go
#check if there is a checker in location and if there is none where that want to go
    #valid= A,C,E,G and 0,2,4,6
    #valid= B,D,F,H and 1,3,5,7
    
#while input is not quit

#if input is valid:
    #re-draw the square with the new checker piece
    #redraw previus square with no checker piece
#if input is not valid:
    #print('move not permited')
    #getattro back to start (ask for new input)


def moveChecker(length):
    bob=turtle.Turtle()
    wn=turtle.Screen()
    place= input("New Checker Location (to quit type quit)=> ")
    validInput=['A0',"A2",'A4','A6','C0','C2','C4','C6','E0','E2','E4','E6',
                'G0','G2','G4','G6','B1','B3','B5','B7','D1','D3','D5','D7',
                'F1','F3','F5','F7','H1','H3','H5','H7']
    oldY= 0
    oldX= -1
    while place!= "quit":
        bob.up()
        if (oldX!=-1):
            if(place in validInput):
                y= int(place[1])
                x= int(ord(place[0])-65)
                drawChecker(bob,wn,x,y,length)
                bob.up()
                bob.goto(oldX,oldY)
                drawSquare(bob,length,"gray")
                oldY= int(place[1])
                oldX= int(ord(place[0])-65)
                drawLabels(bob)
            else:
                print("Invalid Input")
        else:
            if(place in validInput):
                y= int(place[1])
                x= int(ord(place[0])-65)
                drawChecker(bob,wn,x,y,length)
                oldY= int(place[1])
                oldX= int(ord(place[0])-65)
            else:
                print("Invalid Input")
        place= input("New Checker Location (to quit type quit)=> ")
moveChecker(1)





        
