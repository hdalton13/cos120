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
            print("Valid Moves",validMovesList)
            index=int(input("Player " + currentPlayer + " enter your move INDEX => "))
            while index<0 or index>=len(validMovesList):
                index=int(input("Player " + currentPlayer + " enter your move INDEX => "))
            move = validMovesList[index]
        else:
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
            
#Heuristic 4 will keep the backrow full until necessary
            backRowChecks=backRowCheck(board,validMovesList)
            if backRowChecks != False:
                move=backRowChecks[random.randrange(0,len(backRowChecks))]
                #print("Returned @ Make BRChecks",move)
                return move
            
#Heristic 2: will move checker piece into a open edge
            sideOpen= checkForOpenSide(validMovesList)
            print (sideOpen)
            if sideOpen != False:
                return sideOpen
            else:
                move=validMovesList[random.randrange(0,len(validMovesList))]

                #move=validMovesList[random.randrange(0,len(validMovesList))]
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
#Heuristic 4 will keep the backrow full until necessary
            backRowChecks=backRowCheck(board,newJumps)
            if backRowChecks != False:
                move=backRowChecks[random.randrange(0,len(backRowChecks))]
                return move

# Heuristic 5 will take the most amount of checkers
            lenCheck=mostChecks(newJumps)
            if lenCheck!= False:
                move=newJumps[lenCheck]
            else:
                move=backRowChecks[random.randrange(0,len(backRowChecks))]
            return move

            
#Heristic 2 part two: will jump checker piece into a open edge
            kSideOpen= checkForOpenSide(newJumps)
            if kSideOpen != False:
                return kSideOpen
            
        #move=validMovesList[random.randrange(0,len(validMovesList))]

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
    for index in range(len(moves)):
        begRow=ord(moves[index][0])-65
        begCol=int(moves[index][1])
        endRow=ord(moves[index][-2])-65
        endCol=int(moves[index][-1])
        
        if (board[endRow][endCol] == "" and endRow==7):
            return index
    return False
  

def backRowCheck(board,moves):
    lst=[]
    for i in range(len(moves)):
        if moves[i][0]!="A":
            lst.append(moves[i])
    if lst!=[]:
        return lst
    return False

def checkForKing(board,newJumps,currentPlayerTokens,rowInc,opposingPlayerTokens,currentPlayer):
    for index in range(len(newJumps)):
        begRow=ord(newJumps[index][0])-65
        begCol=int(newJumps[index][1])
        colChangeTotal=int(newJumps[index][4])-int(newJumps[index][1])
        colChange=colChangeTotal//2
        if (board[begRow+rowInc][begCol+colChange]==opposingPlayerTokens[1]): 
            return index
    return False

def checkForOpenSide(validMovesList):
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
    validMovesListMY=getValidMovesList(board,currentPlayerTokens,rowInc)
    oppositeJumps=getValidJumpsList(board,opposingPlayerTokens,rowInc*-1,currentPlayerTokens)

    newLst=[]
    for opp in oppositeJumps:
        for mine in validMovesListMY:
            if (opp[-2:]==mine[-2:]):
                newLst.append(mine)
    print(newLst,"NewList")
    
    if len(newLst)<1:
        return False
    else:
        randBLOCK = newLst[random.randrange(0,len(newLst))]
        return randBLOCK




    #getjumps if position in jumps and pos in valid moves[-2][-1] for current player then move to position
    #a1:34

































    
