#11/20/19
###Cant run code because you didn't declare a turtle
import turtle

def tree(trunkLength,t):
    if trunkLength < 5:
        return
    else :
        t.forward(trunkLength)
        t.right(30)
        tree(trunkLength-15 , t)
        t.left(60)
        tree(trunkLength-15 , t)
        t.right(30)
        t.backward(trunkLength)

"""Write a recursive function to compute the sum of a series of numbers from 1 to N"""
def summationR(N):
    if N==1:
        return N
    else:
        return N + summationR(N-1)

'''Write a recursive function to compute the sum of all the numbers in a list.'''
def sumList(alist):
    if alist == [ ]:
        return 0
    else:
        return alist[0] + sumList(alist[1:])

'''Write a recursive function to find the minimum number in a list.'''
def minList(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        if alist[0] < minList(alist[1:]):
            return alist[0]
        else:
            return minList(alist[1:])

print(minList([3,5,2,1,3]))

'''Write a recursive function to find the maximum number in a list.'''
def maxList(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        if alist[0] > maxList(alist[1:]):
            return alist[0]
        else:
            return maxList(alist[1:])

'''Write a recursive function to reverse the characters in a string'''
def revString(aString):
    if aString == “”:
        return “”
    else:
        return revString(aString[1:]) + aString[0]


'''Write a recursive function to decide if a given string is a palindrome.'''
def isPalindrome(aString):
    if len(aString) == 0 or len(aString) == 1:
        return True
    else:
        if aString[0] == aString[-1]:
	return isPalindrome(aString[1:-1])
        else:
	return False

"""Sierpinski Function: constructs three triangles smaller to bigger"""
def drawTriangle(t,p1,p2,p3):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p1)

def midPoint(p1,p2):
    return((p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0)

def sierpinski(myTurtle,p1,p2,p3,depth):
    if depth > 0:
        sierpinski(myTurtle,p1,midPoint(p1,p2),midPoint(p1,p3),depth-1)
        sierpinski(myTurtle,p2,midPoint(p2,p3),midPoint(p2,p1),depth-1)
        sierpinski(myTurtle,p3,midPoint(p3,p1),midPoint(p3,p2),depth-1)
    else:
        drawTriangle(myTurtle,p1,p2,p3)


"""Koch Curves"""
def Koch(aTurtle,distance,depth):
    if depth == 0:
        aTurtle.forward(distance)
    else:
        Koch(aTurtle,distance/3, depth-1)
        aTurtle.left(60)
        Koch(aTurtle,distance/3, depth-1)
        aTurtle.right(120)
        Koch(aTurtle,distance/3, depth-1)
        aTurtle.left(60)
        Koch(aTurtle,distance/3, depth-1)
Koch(bob,200,3)
