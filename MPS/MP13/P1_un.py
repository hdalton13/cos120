#Heather Dalton and Kayla Rehwoldt 

import random

EMPTY=''
INCs=[-1,1]
VALID_RANGE=range(8)

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
                    ((jmp[-2:]+":"+toCoords) not in jmp) and ((toCoords+':'+jmp[-2:] not in jmp)):
#                    ((jmp[-2:]+":"+toCoords) not in jmp) and ((toCoords+':'+jmp[-2:] not in jmp)):
                        newJumps.append(jmp+":"+toCoords)
                        expanded=True
        if not expanded:
            newJumps.append(jmp)
    return newJumps

def getValidPlayerMove(board,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer,auto):
    validMovesList=getValidMovesList(board,currentPlayerTokens,rowInc)
    oldJumps=getValidJumpsList(board,currentPlayerTokens,rowInc,opposingPlayerTokens)
    newJumps=expandJumps(oldJumps,board,rowInc,opposingPlayerTokens)
    move=""
    while newJumps != oldJumps:
        oldJumps=newJumps[:]
        newJumps=expandJumps(oldJumps,board,rowInc,opposingPlayerTokens)
    if newJumps==[]:
        if not auto:
            index=int(input("Player " + currentPlayer + " enter your move INDEX => "))
            while index<0 or index>=len(validMovesList):
                index=int(input("Player " + currentPlayer + " enter your move INDEX => "))
            move = validMovesList[index]
        else:
            if validMovesList==[]:
                return currentPlayer
#Heuristic 3 will prioritize making non-king checkers kings
            makeKingCheck = makeKing(board,validMovesList,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer)
            #print(makeKingCheck)
            if makeKingCheck != False:
                #print("Returned @ Make Checks")
                move=validMovesList[makeKingCheck]
                return move

# Heuristic 6 checks for blocks
            blocks= checkBlocks(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens)
            if blocks != False:
                return blocks
            
# Heuristic 7 will take a checker out of a jump possibility
            noBlocksAv = noBlocks(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens)
            if noBlocksAv!=False:
                return noBlocksAv

            
# Heuristic 9 will move to safe spot
            safe= saveSpot(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens)
            if safe != False:
                return safe
            
#Heristic 10: Control the Center
            control=controlcenter(validMovesList)
            if control!=False:
                return control
            
# Heuristic 8 will sacrifice checker in order to set up jump
            sacrifice = sacrificeIt(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens)
            if sacrifice != False:
                return sacrifice


#Heuristic 4 will keep the backrow full until necessary
            backRowChecks=False
            backRowChecks = backRowCheck(board,validMovesList,currentPlayerTokens)
            if backRowChecks != False:
                checkLst=backRowCheck(board,validMovesList,currentPlayerTokens)
                move=backRowChecks[random.randrange(0,len(checkLst))]
                #print("Returned @ Make BRChecks",move)
                return move
            
#Heristic 2: will move checker piece into a open edge
            sideOpen= checkForOpenSide(validMovesList)
            print (sideOpen)
            if sideOpen != False:
                return sideOpen
            
#Heristic 12: this will take the last item in the lst if nothing else has been selected
            

    else:
        if not auto:
            print("Valid Jumps",newJumps)
            index=int(input("Player " + currentPlayer + " enter your jump INDEX => "))
            while index<0 or index>=len(newJumps):
                index=int(input("Player " + currentPlayer + " enter your jump INDEX => "))
            move = newJumps[index]
        else:
            if len(newJumps)>0:
                if len(newJumps)==1:
                    move=newJumps[0]
                    return move
#Heuristic 3 will prioritize making non-king checkers kings
            
            makeKingCheck = makeKing(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer)
            if makeKingCheck != False:
                move=newJumps[makeKingCheck]
                return move

#Heristic 1: will take jump to delete other king
            
            kingCheck=checkForKing(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer)
            if kingCheck!=False:
                move=newJumps[kingCheck]
                return move
#Heuristic 11 jump checkers to a safe location
            
            safeJumpCheck = safeJump(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer)
            if safeJumpCheck != False:
                return safeJumpCheck
            


# Heuristic 5 will take the most amount of checkers
            
            lenCheck=mostChecks(newJumps)
            if lenCheck!= False:
                move=newJumps[lenCheck]
                return move
            
#Heristic 2 part two: will jump checker piece into a open edge
            kSideOpen= checkForOpenSide(newJumps)
            if kSideOpen != False:
                return kSideOpen
    


#Heristic 12: will jump a random checker  
            jump=newJumps[random.randrange(0,len(newJumps))]
            return jump

#Heuristic 5 jumps most checkers
def mostChecks(jumps):
    longest=len(jumps[0])
    index=0
    for i in range(len(jumps)):
        if len(jumps[i])>longest:
            longest=len(jumps[i])
            index=i
    if longest==5:
        return False
    return index
    
#Heristic 3: If checker is able to become a king move it there
def makeKing(board,moves,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer):
    #print("makeKing")
    for index in range(len(moves)):
        begRow=ord(moves[index][0])-65
        begCol=int(moves[index][1])
        endRow=ord(moves[index][-2])-65
        endCol=int(moves[index][-1])
        
        if (board[endRow][endCol] == "" and endRow==7):
            return index
    return False
  

def backRowCheck(board,moves,currentPlayerTokens):
    #print("backRowCheck")

    lst=[]
    for i in range(len(moves)):
        if "R" in currentPlayerTokens or "r" in currentPlayerTokens:
            if moves[i][0]!="A":
                lst.append(moves[i])
        else:
            if moves[i][0]!="H":
                lst.append(moves[i])
    if lst!=[]:
        return lst
    return False

def checkForKing(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer):
    #print("checkForKing")

    for index in range(len(newJumps)):
        begRow=ord(newJumps[index][0])-65
        begCol=int(newJumps[index][1])
        colChangeTotal=int(newJumps[index][4])-int(newJumps[index][1])
        colChange=colChangeTotal//2
        if (board[begRow+rowInc][begCol+colChange]==opposingPlayerTokens[1]): 
            return index
    return False

def checkForOpenSide(validMovesList):
    #print("checkForOpenSide")

    sideOptions=[]
    for i in validMovesList:
        if int(i[4])==0 or int(i[4])==7:
            sideOptions.append(i)
    if len(sideOptions)>1:
        sideMove = sideOptions[random.randrange(0,len(sideOptions))]
        return sideMove
    else:
        return False

def checkBlocks(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens):
    #print("checkBlocks")

    validMovesListMY=getValidMovesList(board,currentPlayerTokens,rowInc)
    oppositeJumps=getValidJumpsList(board,opposingPlayerTokens,rowInc*-1,currentPlayerTokens)
    newLst=[]
    for opp in oppositeJumps:
        for mine in validMovesListMY:
            if (opp[-2:]==mine[-2:]):
                newLst.append(mine)
    
    if len(newLst)<1:
        return False
    else:
        randBLOCK = newLst[random.randrange(0,len(newLst))]
        return randBLOCK

#Heuristic 7
def noBlocks(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens):
    #print("noBlocks")

    validMovesListMY=getValidMovesList(board,currentPlayerTokens,rowInc)
    oppositeJumps=getValidJumpsList(board,opposingPlayerTokens,rowInc*-1,currentPlayerTokens)
    newLst=[]
    for opp in oppositeJumps:
        for mine in validMovesListMY:
            oppRow= ord(opp[0])-65
            oppCol= opp[1]            
            jumpRow= int(oppRow) - int(rowInc)
            if jumpRow == ord(mine[0])-65 and int(oppCol) - int(rowInc) == int(mine[1]):
                newLst.append(mine)
    if len(newLst)>=1:
        randMove = newLst[random.randrange(0,len(newLst))]
        return randMove
    return False
        
#Heuristic 8          
def sacrificeIt(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens):

    validMovesListMY=getValidMovesList(board,currentPlayerTokens,rowInc)
    
    for mine in validMovesListMY:
        myRow=ord(mine[0])-65
        myCol=int(mine[1])
        checkOpRow= int(myRow +(2*rowInc))
        checkSupportRow= myRow-rowInc
        checkSupportCol=myCol-1
        if checkSupportCol<0 or checkSupportRow<0:
            return False
        if board[checkOpRow][myCol] in opposingPlayerTokens and board[checkSupportRow][checkSupportCol] in currentPlayerTokens:
            #print("Thank goodness")
            return mine
        return False
    

    #getjumps if position in jumps and pos in valid moves[-2][-1] for current player then move to position
    #a1:34


def saveSpot(board,oldJumps,currentPlayerTokens,rowInc,opposingPlayerTokens):
    #print("saveSpot")

    validMovesListMY=getValidMovesList(board,currentPlayerTokens,rowInc)
    lst=["B","r","b","R"]
    for mine in validMovesListMY:
        myRow=ord(mine[0])-65
        myCol=int(mine[1])
        
        checkRow = int(myRow +(2*rowInc))
        checkColM = int(myCol-2)
        checkColP = int(myCol+2)
        if checkColM >7 or checkColM <0:
            return False
        if checkColP >7 or checkColP <0:
            return False

        if (board[myRow][checkColM] in lst and board[checkRow][myCol] in lst) or (board[myRow][checkColP] in lst and board[checkRow][myCol] in lst):
            return mine
        
    return False


def controlcenter(movesLst):
    centerOboard=["E2","E4","D3","D5"]
    moves=[]
    for i in movesLst:
        if i[3:] in centerOboard:
            moves.append(i[:])
    if moves!=[]:
        rand=moves[random.randrange(0,len(moves))]
        #print(rand)
        return rand
    return False
    
def safeJump(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer):
    newLst=[]

    for move in newJumps:
        myRow=ord(move[-2])-65
        myCol=int(move[-1])
        if board[myRow+rowInc][myCol-1] not in opposingPlayerTokens or board[myRow+rowInc][myCol+1]  not in opposingPlayerTokens:
            newLst.append(move)

    if len(newLst)>=1:
        randMove = newLst[random.randrange(0,len(newLst))]
        return randMove
    return False
        
    














    
