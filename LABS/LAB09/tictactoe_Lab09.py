import turtle
""" The initial phases of a tic/tac/toe game!!!!
Add the following functionality to the game:
1) Randomly select X or O to go first (10 points)
2) Allow the player to specify where to place a marker, using
the input form:  0,0  or  1,0  or  2,2  etc. (10 points)
3) Draw the appropriate marker there, if the square is not
already occupied (20 points)
4) Alternating players, continue to allow placement of markers
until EXIT is entered for a move (20 points)
5) Do not accept invalid moves from the player.  In this game version,
a valid move is any of the squares, 0,1,2 row and column, if the square is
not occupied (20 points)
6) When a legal move is made, make sure the logical board is updated as
well as the physical board (20 points)

DO NOT WORRY ABOUT CHECKING FOR WINS
We will work on the rest of the game logic in class tomorrow!!!!
"""

def DrawTicTacToeBoard(t,wn):
    wn.tracer(False)
    #Vertical Lines of board
    t.pensize(3)
    t.up()
    t.goto(.5,-.5)
    t.down()
    t.goto(.5,2.5)
    t.up()
    t.goto(1.5,-.5)
    t.down()
    t.goto(1.5,2.5)
    #Horizontal Lines of board
    t.up()
    t.goto(-.4,.5)
    t.down()
    t.goto(2.4,.5)
    t.up()
    t.goto(-.4,1.5)
    t.down()
    t.goto(2.4,1.5)
    wn.tracer(True)

def writeMarker(t,marker,row,col):
    t.up()
    t.goto(row,col+.25)
    t.down()
    t.write(marker,align='center',font=("Arial",32,"bold"))

def switch(player):
    if player=="X":
        return "O"
    else:
        return "X"
import random

def main():
    r=["","",""]
    tt=[r[:],r[:],r[:]]
    wn=turtle.Screen()
    joe=turtle.Turtle()
    wn.setworldcoordinates(-1,5,5,-1)
    joe.ht()
    DrawTicTacToeBoard(joe,wn)
    player=""
#1
    rand= random.randrange(2)
    if rand == 1:
        player="X"
    else:
        player="O"

    print("First player=",player)
#2-6
    placement=input("Write your move( format 0,0 ) or ('exit' if you want to quit)=>")
    validM=["0,0","0,1","0,2","1,0","1,1","1,2","2,0","2,1","2,2",]
    while placement!= "exit":
        if(placement in validM) and tt[int(placement[0])][int(placement[-1])]=="":
            row= int(placement[0])
            col= int(placement[-1])
            writeMarker(joe,player,row,col)
            tt[row][col]=player
            player= switch(player)
        else:
            print("Invalid")
        placement=input("Write your move( format 0,0 ) or ('exit' if you want to quit)=>")
    

    
main()
