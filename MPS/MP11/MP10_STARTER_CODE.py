import turtle
import random
import P1
import P2

EMPTY=''
INCs=[-1,1]
VALID_RANGE=range(8)

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
    drawCircleFilled(t) #the outer checker circle
    #draws the checker rings
    for i in range(1,5,1):
        t.up()
        t.goto(x,y+(i*.1))
        t.down()
        t.circle((5-i)*.2*.5)
    #determine if a 'r' has moved into row 7, or a 'b' into row 0 - KING ME
    #change the player letter to uppercase
    if playerToken=='r' and row==7:
        playerToken="R"
    elif playerToken=="b" and row==0:
        playerToken="B"
    board[row][col]=playerToken
    #add a star or a K to the checker in question
    if playerToken in ['R','B']:
        t.up()
        t.color("yellow")
        t.goto(x,y+.8)
        t.write("K",align="center",font=("Arial",28,"bold"))
        t.down()
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
    
def populateOldGame(t,wn,board):
    outFile=open("checkBlocks.txt","r")
    currentPlayer=outFile.readline()[:-1]
    lstLines=outFile.readlines()
    for row in range(len(lstLines)):
        for col in range(len(lstLines[row])-1):
            if (row+col)%2==0 and lstLines[row][col] != 'e':
                    drawChecker(t,wn,row,col,board,lstLines[row][col])
    return currentPlayer

def populateNewGame(t,wn,board):
    for row in range(0,3,1):
        for col in range(8):
            if (row+col)%2==0:
                drawChecker(t,wn,row,col,board,"r")
    for row in range(5,8,1):
        for col in range(8):
            if (row+col)%2==0:
                drawChecker(t,wn,row,col,board,"b")

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
    playerToken=board[row][col]
    board[row][col]=""
    drawLabel(bob,row,col)
    return playerToken

def parseMove(move):
    fromRow=ord(move[0])-65
    fromCol=int(move[1])
    toRow=ord(move[3])-65
    toCol=int(move[4])
    return fromRow,fromCol,toRow,toCol

def switchPlayers(currentPlayer):
    if currentPlayer=="Black":
        currentPlayer="Red"
        currentPlayerTokens=['r','R']
        opposingPlayerTokens=['b','B']
        rowInc=1
    else:
        currentPlayer="Black"
        currentPlayerTokens=['b','B']
        opposingPlayerTokens=['r','R']
        rowInc=-1
    return currentPlayer,currentPlayerTokens,rowInc,opposingPlayerTokens

#function to return a list of all valid moves for the current player
def getValidMovesList(board,currentPlayerTokens,rowInc):
    validMovesList=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if board[row][col] in ['r','b']: #regular checker
                    for colInc in [-1,1]:
                        if (col+colInc)>=0 and (col+colInc)<=7 and (row+rowInc)>=0 and (row+rowInc)<=7 and board[row+rowInc][col+colInc]=="":
                            validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rowInc+65)+str(col+colInc))
                else: #king
                    for rInc in [1,-1]:
                        for cInc in [-1,1]:
                            if (col+cInc)>=0 and (col+cInc)<=7 and (row+rInc)>=0 and (row+rInc)<=7 and board[row+rInc][col+cInc]=="":
                                validMovesList.append(chr(row+65)+str(col)+":"+chr(row+rInc+65)+str(col+cInc))                    
    return validMovesList

#function to return a list of all valid jumps for the current player
def getValidJumpsList(board,currentPlayerTokens,rowInc,opposingPlayerTokens): #Not finished
    lst=[]
    for row in range(8):
        for col in range(8):
            if board[row][col] in currentPlayerTokens:
                if board[row][col] in ['r','b']: #regular checker
                    for colInc in [-1,1]:
                        if (col+2*colInc)>=0 and (col+2*colInc)<=7 and (row+2*rowInc)>=0 and (row+2*rowInc)<=7 and  board[row+rowInc][col+colInc] in opposingPlayerTokens and board[row+2*rowInc][col+2*colInc]=='': 
                            lst.append(chr(row+65)+str(col)+":"+chr(row+(2*rowInc)+65)+str(col+(2*colInc)))
                else: #king
                    for rInc in [1,-1]:
                        for cInc in [-1,1]:
                            if (col+2*cInc)>=0 and (col+2*cInc)<=7 and (row+2*rInc)>=0 and (row+2*rInc)<=7 and board[row+rInc][col+cInc] in opposingPlayerTokens and board[row+2*rInc][col+2*cInc]=='': 
                                lst.append(chr(row+65)+str(col)+":"+chr(row+(2*rInc)+65)+str(col+(2*cInc)))                            
    return lst

def expandJumps(oldJumps,board,rowInc,opposingPlayerTokens):
    newJumps=[]
    for jmp in oldJumps:
        initiatingRow=ord(jmp[0])-65
        initiatingCol=int(jmp[1])
        tokenType=board[initiatingRow][initiatingCol] #whole purpose of looking at first square is to get token type

        endRow=ord(jmp[-2])-65              #becomes starting row for next jump
        endCol=int(jmp[-1])                 #becomes starting columns for next jump
        
        #newJumps.append(jmp)
        expanded=False
        if tokenType in ["r","b"]:          #regular checker
            for colInc in [-1,1]:
                jumpOverRow=endRow+rowInc
                jumpOverCol=endCol+colInc
                toRow=endRow+2*rowInc
                toCol=endCol+2*colInc
                if toRow in VALID_RANGE and toCol in VALID_RANGE and board[jumpOverRow][jumpOverCol] in opposingPlayerTokens and board[toRow][toCol]==EMPTY:
                    newJumps.append(jmp+":"+chr(toRow+65)+str(toCol))
                    expanded=True
        else:#king checker
            for rInc in [1,-1]:
                for cInc in [-1,1]:
                    jumpOverRow=endRow+rInc
                    jumpOverCol=endCol+cInc
                    toRow=endRow+2*rInc
                    toCol=endCol+2*cInc
                    toCoords=chr(toRow+65)+str(toCol)
                    if toRow in VALID_RANGE and toCol in VALID_RANGE and board[jumpOverRow][jumpOverCol] in opposingPlayerTokens and \
                    (board[toRow][toCol]==EMPTY or toCoords==jmp[0:2]) and \
                    ((jmp[-2:]+":"+toCoords) not in jmp):
                        newJumps.append(jmp+":"+toCoords)
                        expanded=True
        if not expanded:
            newJumps.append(jmp)
    return newJumps

def setupGame(newGame):
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
    if newGame:
        populateNewGame(bob,wn,board)
        currentPlayer=["Red","Black"][random.randint(0,1)]
    else:
        currentPlayer=populateOldGame(bob,wn,board)
    if currentPlayer=="Red":
        currentPlayerTokens=['r','R']
        opposingPlayerTokens=['b','B']
        rowInc=1
    else:
        currentPlayerTokens=['b','B']
        opposingPlayerTokens=['r','R']
        rowInc=-1
    return board,bob,wn,currentPlayer,currentPlayerTokens,opposingPlayerTokens,rowInc

def win(board): #must add unable to move - hey, is there an easier way?
    blackCount=0
    redCount=0
    #print(board)
    for row in board:
        for col in row:
            if col in ['r','R']:
                redCount+=1
            elif col in ['b','B']:
                blackCount+=1
    if blackCount>=1 and redCount>=1:
        return [False,""]
    elif blackCount==0:
        return [True,"Red"]
    else:
        return [True,"Black"]

def saveGame(currentPlayer,board):
    outFile=open("test.txt","w")
    outFile.write(currentPlayer+"\n")
    for row in board:
        rowString=""
        for col in row:
            if col == '':
                rowString+='e'
            else:
                rowString+=col
        outFile.write(rowString+"\n")
    outFile.close()
    
def checkers():
    #auto=True
    newGame=False
    board,bob,wn,currentPlayer,currentPlayerTokens,opposingPlayerTokens,rowInc=setupGame(newGame)
    if currentPlayer=="Red":
        move=P1.getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto=True)
    else:
        move=P2.getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto=False)
    while move != 'QUIT' and not win(board)[0]:
        fromRow,fromCol,toRow,toCol=parseMove(move)
        #Hmmm, this if else code looks like it may belong in a new function
        if abs(fromRow-toRow)==1: #a move is legal (no jumps available)
            playerToken=removeChecker(bob,board,fromRow,fromCol)
            drawChecker(bob,wn,toRow,toCol,board,playerToken)
        else: #a jump is available
            while len(move)>=5:
                fromRow,fromCol,toRow,toCol=parseMove(move)
                playerToken=removeChecker(bob,board,(fromRow+toRow)//2,(fromCol+toCol)//2) #remove opposing player
                playerToken=removeChecker(bob,board,fromRow,fromCol) #remove jumper
                drawChecker(bob,wn,toRow,toCol,board,playerToken)    #redraw jumper
                move=move[3:]
        currentPlayer,currentPlayerTokens,rowInc,opposingPlayerTokens=switchPlayers(currentPlayer)
        if not win(board)[0]:
            if currentPlayer=="Red":
                move=P1.getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto=True)
            else:
                move=P2.getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto=False)
    if move=='QUIT':
        saveGame(currentPlayer,board)
    else:
        print("Winner is player",win(board)[1]+"!!!")

checkers()
