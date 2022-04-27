import turtle
import random

"""Dr. White told us to work as far as we could and then submit what we have with what we still have to complete"""
###  --> Note: His origional code allows non-king players to jump backwards: can't figure out how to change it
###  --> So far everything is working for only double jumps
###  --> All I need to do now is somehow generalize expandedJumps to be able to make it able to do more than just a double jump
###  --> THIS WORKS= ['G4:E2:C4', 'G4:E6:C4'] """i JUST CAN'T ADD ONTO WHAT I HAVE"""
###  --> THIS DOESN'T WORKS= ['G4:E2:C4:E6', 'G4:E6:C4:E2']
###  --> THIS DOESN'T WORKS= ['G4:E2:C4:E6:G4', 'G4:E6:C4:E2:G4']
###  --> I generalized all of the other code so once I have a larger expanded Jumps it should word


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
        t.goto(x,y+.8)
        t.color("Yellow")
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
    outFile=open("test.txt","r")
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
    if len(move)<=5:
        fromRow=ord(move[0])-65
        fromCol=int(move[1])
        toRow=ord(move[3])-65
        toCol=int(move[4])
        return fromRow,fromCol,toRow,toCol
    else:
        moveLST=move.split(":")
        length=(len(moveLST))
        print(moveLST)
        print(length)
        return moveLST, length

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
                        if (col+colInc)>=0 and (col+colInc)<=7 and (row+rowInc)>=0 and (row+rowInc)<=7 and board[row+rowInc][col+colInc] in opposingPlayerTokens and (col+2*colInc)>=0 and (col+2*colInc)<=7 and row+(2*rowInc)>=0 and row+(2*rowInc)<=7 and board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                            lst.append(chr(row+65)+str(col)+":"+chr(row+(2*rowInc)+65)+str(col+(2*colInc)))
                else: #king
                    for rInc in [1,-1]:
                        for cInc in [-1,1]:
                            if (col+cInc)>=0 and (col+cInc)<=7 and (row+rInc)>=0 and (row+rInc)<=7 and board[row+rInc][col+cInc] in opposingPlayerTokens and (col+2*cInc)>=0 and (col+2*cInc)<=7 and row+(2*rInc)>=0 and row+(2*rInc)<=7 and board[row+(2*rInc)][col+(2*cInc)]=='' : 
                                lst.append(chr(row+65)+str(col)+":"+chr(row+(2*rInc)+65)+str(col+(2*cInc)))                            
    return lst

def DOUBLEJUMPSexpandJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens):
    lst2= getValidJumpsList(board,currentPlayerTokens,rowInc,opposingPlayerTokens)
    lst=[]
    for i in lst2:
        row= ord(i[3])-65
        col= int(i[4])
        og=i[:3]
        #print(row,col)
        
        if board[row][col] in ['r','b']: #regular checker
            for colInc in [-1,1]:
                if (col+colInc)>=0 and (col+colInc)<=7 and (row+rowInc)>=0 and (row+rowInc)<=7 and board[row+rowInc][col+colInc] in opposingPlayerTokens and (col+2*colInc)>=0 and (col+2*colInc)<=7 and row+(2*rowInc)>=0 and row+(2*rowInc)<=7 and board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                    doubleJ=og+chr(row+65)+str(col)+":"+chr(row+(2*rowInc)+65)+str(col+(2*colInc))
                    lst.append(doubleJ)
        else: #king
            for rInc in [1,-1]:
                for cInc in [-1,1]:
                    if (col+cInc)>=0 and (col+cInc)<=7 and (row+rInc)>=0 and (row+rInc)<=7 and board[row+rInc][col+cInc] in opposingPlayerTokens and (col+2*cInc)>=0 and (col+2*cInc)<=7 and row+(2*rInc)>=0 and row+(2*rInc)<=7 and board[row+(2*rInc)][col+(2*cInc)]=='' : 
                        KdoubleJ=og+chr(row+65)+str(col)+":"+chr(row+(2*rInc)+65)+str(col+(2*cInc))
                        lst.append(KdoubleJ)
    #print(lst)
    return lst

def expandJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens,lst2):
    lst=[]
    for i in lst2:
        row= ord(i[-2])-65
        col= int(i[-1])
        og=i[:3]
        #print(row,col)
        
        if board[row][col] in ['r','b']: #regular checker
            for colInc in [-1,1]:
                if (col+colInc)>=0 and (col+colInc)<=7 and (row+rowInc)>=0 and (row+rowInc)<=7 and board[row+rowInc][col+colInc] in opposingPlayerTokens and (col+2*colInc)>=0 and (col+2*colInc)<=7 and row+(2*rowInc)>=0 and row+(2*rowInc)<=7 and board[row+(2*rowInc)][col+(2*colInc)]=='' : 
                    doubleJ=og+chr(row+65)+str(col)+":"+chr(row+(2*rowInc)+65)+str(col+(2*colInc))
                    lst.append(doubleJ)
        else: #king
            for rInc in [1,-1]:
                for cInc in [-1,1]:
                    if (col+cInc)>=0 and (col+cInc)<=7 and (row+rInc)>=0 and (row+rInc)<=7 and board[row+rInc][col+cInc] in opposingPlayerTokens and (col+2*cInc)>=0 and (col+2*cInc)<=7 and row+(2*rInc)>=0 and row+(2*rInc)<=7 and board[row+(2*rInc)][col+(2*cInc)]=='' : 
                        KdoubleJ=og+chr(row+65)+str(col)+":"+chr(row+(2*rInc)+65)+str(col+(2*cInc))
                        lst.append(KdoubleJ)
    #print(lst)
    return lst


def getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto):
    validMovesList=getValidMovesList(board,currentPlayerTokens,rowInc)
    validJumpsList=getValidJumpsList(board,currentPlayerTokens,rowInc,opposingPlayerTokens)
    changed=validJumpsList[:]
    print(changed)
    expandsJumpslst=expandJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens,changed)
    five=5
   
###this is giving me an endless loop of random 3 jumps
##"""
##    while changed != expandsJumpslst and five!=0:
##        changed=expandsJumpslst[:]
##        print(changed)
##        expandsJumpslst = expandJumps(board,currentPlayerTokens,rowInc,opposingPlayerTokens,changed)
##        print(expandsJumpslst)
##        five-=1
##"""
    if validJumpsList==[]:
        if not auto:
            print("Valid Moves",validMovesList)
            move=input("Player " + currentPlayer + " enter your move => ").upper()
            while move !="QUIT" and move not in validMovesList:
                move=input("Player " + currentPlayer + " enter your move => ").upper()
        else:
            if len(validMovesList)>0:
                move=validMovesList[random.randrange(0,len(validMovesList))]
    else:
        if not auto:
            if expandsJumpslst==[]:
                print("Valid Jumps",validJumpsList)
                move=input("Player " + currentPlayer + " enter your jump => ").upper()
                while move !="QUIT" and move not in validJumpsList:
                    move=input("Player " + currentPlayer + " enter your jump => ").upper()
            else:
                print("Multiple Jumps",expandsJumpslst)
                move=input("Player " + currentPlayer + " enter your jump => ").upper()
                while move !="QUIT" and move not in expandsJumpslst:
                    move=input("Player " + currentPlayer + " enter your jump => ").upper()
        else:
            move=validJumpsList[random.randrange(0,len(validJumpsList))]
    return move

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

def win(board):
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
    auto=False
    newGame=False
    board,bob,wn,currentPlayer,currentPlayerTokens,opposingPlayerTokens,rowInc=setupGame(newGame)
    move=getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto)
    while move != 'QUIT' and not win(board)[0]:
        if len(move)==5:
            fromRow,fromCol,toRow,toCol=parseMove(move)
            if abs(fromRow-toRow)==1: #a move is legal (no jumps available)
                playerToken=removeChecker(bob,board,fromRow,fromCol)
                drawChecker(bob,wn,toRow,toCol,board,playerToken)
            else: #a jump is available
                playerToken=removeChecker(bob,board,(fromRow+toRow)//2,(fromCol+toCol)//2) #remove opposing player
                playerToken=removeChecker(bob,board,fromRow,fromCol) #remove jumper
                drawChecker(bob,wn,toRow,toCol,board,playerToken)    #redraw jumper
            currentPlayer,currentPlayerTokens,rowInc,opposingPlayerTokens=switchPlayers(currentPlayer)
            if not win(board)[0]:
                move=getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto)
        else:
            moveLST, length = parseMove(move)
            for i in range(length):
                print(moveLST)
                fromRow= ord(moveLST[0][0])-65
                fromCol= int(moveLST[0][1])
                toRow= ord(moveLST[1][0])-65
                toCol= int(moveLST[1][1])
                moveLST.pop(0)

                if abs(fromRow-toRow)==1: #a move is legal (no jumps available)
                    playerToken=removeChecker(bob,board,fromRow,fromCol)
                    drawChecker(bob,wn,toRow,toCol,board,playerToken)
                else: #a jump is available
                    playerToken=removeChecker(bob,board,(fromRow+toRow)//2,(fromCol+toCol)//2) #remove opposing player
                    playerToken=removeChecker(bob,board,fromRow,fromCol) #remove jumper
                    drawChecker(bob,wn,toRow,toCol,board,playerToken)    #redraw jumper
                if len(moveLST)%length==1:
                    break

            showLogicalBoard(board)
                
            currentPlayer,currentPlayerTokens,rowInc,opposingPlayerTokens=switchPlayers(currentPlayer)
            if not win(board)[0]:
                move=getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto)                
        
    if move=='QUIT':
        saveGame(currentPlayer,board)
    else:
        print("Winner is player",win(board)[1]+"!!!")


checkers()
