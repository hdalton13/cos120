import turtle

validSquares=['A0','A2','A4','A6','B1','B3','B5','B7',
                'C0','C2','C4','C6','D1','D3','D5','D7',
                'E0','E2','E4','E6','F1','F3','F5','F7',
                'G0','G2','G4','G6','H1','H3','H5','H7','QUIT']

def drawSquare(t,color):
    t.color("black",color)
    t.begin_fill()
    for num in range(4):
        t.forward(1)
        t.left(90)
    t.end_fill()

def drawRow(t,color1,color2):
    for i in range(4):
        drawSquare(t,color1)
        t.forward(1)
        drawSquare(t,color2)
        t.forward(1)

def drawCircleFilled(t):
    t.begin_fill()
    t.circle(.5)
    t.end_fill()

def drawChecker(t,wn,row,col,board,playerToken):
    wn.tracer(False)
    t.up()
    t.goto(0,0)
    t.down()
    y=row
    x=col+.5
    if playerToken in ["b","B"]:
        t.color("gray","black")
    else:
        t.color("black","red")
    t.up()
    t.goto(x,y)
    t.down()
    drawCircleFilled(t)
    #rewrite as a loop
    for i in range(1,5,1):
        t.up()
        t.goto(x,y+(i*.1))
        t.down()
        t.circle((5-i)*.2*.5)
    board[row][col]=playerToken
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

def drawBoard(t,wn):
    wn.tracer(False)
    c1="gray"
    c2="red"
    for x in range(8):
        drawRow(t,c1,c2)
        t.backward(8)
        t.left(90)
        t.forward(1)
        t.right(90)
        #switch c1 and c2 contents
        temp=c1
        c1=c2
        c2=temp
    wn.tracer(True)

def setupGame():
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,9,9,-1)
    bob=turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    drawBoard(bob,wn)
    drawLabels(bob,wn)
    row=['','','','','','','','']
    board=[]
    for i in range(8):
        board.append(row[:])
    return board,bob,wn

def populateNewGame(t,wn,board):
    for row in range(0,3,1):
        for col in range(8):
            if (row+col)%2==0:
                drawChecker(t,wn,row,col,board,"r")
    for row in range(5,8,1):
        for col in range(8):
            if (row+col)%2==0:
                drawChecker(t,wn,row,col,board,"b")
    showLogicalBoard(board)

def showLogicalBoard(board):
    for row in board:
        for col in row:
            if col=="":
                print('_',end="")
            else:
                print(col,end="")
        print()

def removeChecker(bob,board,row,col):
    bob.up()
    bob.goto(col,row)
    bob.down()
    drawSquare(bob,"gray")
    board[row][col]=""
    drawLabel(bob,row,col)

def parseMove(move):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    return fromRow,fromCol,toRow,toCol

def switchPlayers(currentPlayer,currentPlayerTokens):
    if currentPlayer=="Black":
        currentPlayer="Red"
        currentPlayerTokens=['r','R']
        enemyTokens=['b','B']
        rowInc=1
    else:
        currentPlayer="Black"
        currentPlayerTokens=['b','B']
        enemyTokens=['r','R']
        rowInc=-1
    return currentPlayer,currentPlayerTokens,rowInc,enemyTokens

#function to return a list of all valid moves for the current player
def getValidMovesList(board,currentPlayerTokens,rowInc): #right now only for player Black
    validMovesList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if col-1>=0 and row+rowInc>=0 and board[row+rowInc][col-1]=="":  #left diagonal only
                    validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col-1))                
                if col+1<=7 and row+rowInc>=0 and board[row+rowInc][col+1]=="":  #right diagonal only
                    validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+1))                
    return validMovesList

def getValidJumpsList(board,currentPlayerTokens,rowInc,enemyTokens): #UNCOMPLETE write the rest of this
    validJumpsList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if (col-2>=0 and row+(rowInc*2)>=0) and (board[row+rowInc][col-1] in enemyTokens):  #left diagonal only
                    validJumpsList.append(chr(row+65)+str(col)+":"+chr(row+(rowInc*2)+65)+str(col-2))
                if (col+2<=7 and row+(2*rowInc)>=0) and (board[row+rowInc][col+1] in enemyTokens):  #right diagonal only
                    validJumpsList.append(chr(row+65)+str(col)+":"+chr(row+(rowInc*2)+65)+str(col+2))                
    return validJumpsList

def getValidPlayerMove(bob,board,currentPlayerTokens,rowInc,enemyTokens):
    validMovesList=getValidMovesList(board,currentPlayerTokens,rowInc)
    validJumpsList=getValidJumpsList(board,currentPlayerTokens,rowInc,enemyTokens)
    position=input("Enter location to move checker ('QUIT' to quit)=> ")
    if position!="QUIT":
        if validJumpsList != []:
            if position in validJumpsList:
                if position[4]<position[1]:
                    rowP=(ord(position[0])+rowInc)-65
                    colP=int(position[1])-1
                    removeChecker(bob,board,rowP,colP)
                    return position
                elif position[4]>position[1]:
                    rowP=(ord(position[0])+rowInc)-65
                    colP=int(position[1])+1
                    removeChecker(bob,board,rowP,colP)
                    return position
            else:
                print("Must be a JUMP:", validJumpsList)
                return "Invalid"
        else:
            if position in validMovesList:
                return position
            else:
                print("Must be a Valid Move", validMovesList)
                return "Invalid"
    else:
        return "QUIT"


def checkers():
    board,bob,wn=setupGame()
    populateNewGame(bob,wn,board)
    currentPlayer="Black"
    currentPlayerTokens=['b','B']
    enemyTokens=['r','R']
    rowInc=-1
    
##    while move != 'QUIT':
##        while move !='QUIT' and (len(move)!=5 or move[0:2] not in validSquares or move[3:] not in validSquares):
##            move=input("Player "+currentPlayer+" enter location to move a checker => ")
##        if move !='QUIT':
##            fromRow,fromCol,toRow,toCol=parseMove(move)
##            if board[fromRow][fromCol] in currentPlayerTokens and board[toRow][toCol]=="":
##                playerToken=board[fromRow][fromCol]
##                removeChecker(bob,board,fromRow,fromCol)
##                drawChecker(bob,wn,toRow,toCol,board,playerToken)
##                showLogicalBoard(board)
##                currentPlayer,currentPlayerTokens,rowInc,enemyTokens=switchPlayers(currentPlayer,currentPlayerTokens)
##            move=input("Player "+currentPlayer+" enter location to move a checker => ")

  
    move=getValidPlayerMove(bob,board,currentPlayerTokens,rowInc,enemyTokens)
    while move != 'QUIT':
        if move!= "Invalid":
            fromRow,fromCol,toRow,toCol=parseMove(move)
            removeChecker(bob,board,fromRow,fromCol)
            drawChecker(bob,wn,toRow,toCol,board,currentPlayerTokens[0])
            currentPlayer,currentPlayerTokens,rowInc,enemyTokens=switchPlayers(currentPlayer,currentPlayerTokens)
        move=getValidPlayerMove(bob,board,currentPlayerTokens,rowInc,enemyTokens)

    turtle.bye()


## Do we need to remove a checker after jumping it?
        
checkers()










