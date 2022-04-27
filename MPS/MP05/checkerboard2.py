import turtle

validMovesList=['A0','A2','A4','A6','B1','B3','B5','B7',
                'C0','C2','C4','C6','D1','D3','D5','D7',
                'E0','E2','E4','E6','F1','F3','F5','F7',
                'G0','G2','G4','G6','H1','H3','H5','H7','quit']

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

def drawChecker(t,wn,row,col,size,currentPlayer):
    wn.tracer(False)
    t.up()
    t.goto(0,0)
    t.down()
    y=(row*size)
    x=(col*size)+(.5*size)
    if currentPlayer=="b":
        color="black"
    else:
        color="red"
    t.color('black',color)
    t.fillcolor(color)
    t.up()
    t.goto(x,y)
    t.down()
    drawCircleFilled(t,size,color)
    for i in range(1,5,1):
        t.up()
        t.goto(x,y+(i*.1)*size)
        t.down()
        t.circle((5-i)*.2*size*.5)
    wn.tracer(True)

def drawLabels(t,wn):
    wn.tracer(False)
    t.up()
    t.color("white")
    for row in range (0,8,1):
        if row%2==0:
            start=0
        else:
            start=1
        for col in range(start,8,2):
            t.goto(col+.75,row+1.02)
            t.write(chr(65+row)+str(col))
    t.color("black")
    wn.tracer(True)

def drawLabel(t,row,col):
    t.color("white")
    t.up()
    t.goto(col+.75,row+1.02)
    t.down()
    t.write(chr(65+row)+str(col))
    t.color("black")

def drawBoard(t,wn,length):
    wn.tracer(False)
    c1="gray"
    c2="red"
    for x in range(8):
        drawRow(t,length,c1,c2)
        t.backward(8*length)
        t.left(90)
        t.forward(length)
        t.right(90)
        #switch c1 and c2 contents
        temp=c1
        c1=c2
        c2=temp
    wn.tracer(True)

def setupGame(length):
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,9,9,-1)
    bob=turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    drawBoard(bob,wn,length)
    drawLabels(bob,wn)
    board=[]
    row=["",'','','','','','','']
    for i in range(8):
        board.append(row[:])
    return bob,wn,board

def removeChecker(bob,row,col,length):
    bob.up()
    bob.goto(col,row)
    bob.down()
    drawSquare(bob,length,"gray")
    drawLabel(bob,row,col)
    

def logicBoard(board):  #this function will put the checkers on the board for a new game

#square by square in first three rows add red checkers to valid squares
    for i in range(0,4,2):
        for j in range(0,8,2):
            if i%2==0:
                board[i][j]='r'
    for j in range(1,8,2):
            if j%2!=0:
                board[1][j]='r'
#square by square in last three rows add black checkers to valid squares                
    for i in range(5,8,2):
        for j in range(1,8,2):
            if i%2!=0:
                board[i][j]='b'
    for j in range(0,8,2):
            if j%2==0:
                board[6][j]='b'
    return board

def drawStartBoard(bob,wn,board,length):
        for i in range(0,4,2):
            for j in range(0,8,2):
                if i%2==0:
                    drawChecker(bob,wn,i,j,length,board[i][j])
                    
        for j in range(1,8,2):
                if j%2!=0:
                    drawChecker(bob,wn,1,j,length,board[1][j])
                    
        for i in range(5,8,2):
            for j in range(1,8,2):
                if i%2!=0:
                    drawChecker(bob,wn,i,j,length,board[i][j])
                    
        for j in range(0,8,2):
                if j%2==0:
                    drawChecker(bob,wn,6,j,length,board[6][j])

def checkPlace(board,fromRow, fromCol, toRow, toCol,currentPlayer):
    if board[toRow][toCol]=='':
        if board[fromRow][fromCol]==currentPlayer:
            board[toRow][toCol]=currentPlayer
            board[fromRow][fromCol]=''
            return True
        else:
            print("Aaaaaaaahhh try again")

def switchPlayer(currentPlayer):
    if currentPlayer=='b':
        return ('r')
    else:
        return ('b')

def checkers(length):
    bob,wn,board=setupGame(length)
    board=logicBoard(board)
    drawStartBoard(bob,wn,board,length)
    move=""
    currentPlayer='b'
    move=input("Enter location to move a checker formate(A1:B2), quit to exit => ")
    while move != 'quit':
        while len(move)!=5 or (move[0:2] not in validMovesList) or (move[3:] not in validMovesList):
            move=input("Enter location to move a checker formate(A1:B2), quit to exit => ")
        
        if move!="quit":
            fromRow= ord(move[0])-65
            fromCol= int(move[1])
            toRow= ord(move[3])-65
            toCol= int(move[4])
            check=checkPlace(board,fromRow, fromCol, toRow, toCol,currentPlayer)
            if check==True:
                removeChecker(bob,fromRow,fromCol,length)
                drawChecker(bob,wn,toRow,toCol,length, currentPlayer)
                currentPlayer=switchPlayer(currentPlayer)
            else:
                print("Invalid move")
            move=input("Enter location to move a checker, quit to exit => ")
    turtle.bye()
        
checkers(1)









