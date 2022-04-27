#Heather Dalton
#09/17/2019

from math import *

#1A
def demoCalls():
    sqrt(16)
    print(sqrt(16))
    x=sqrt(16)
    print(x)
    y=sqrt(16) * sqrt(25)
    print(y)

#I predict that when you call demoCalls(), you will see this printed
#>>>4
#>>>4
#>>>20
#demoCalls()

#1B
def mySQRT(n,iters):
    X=1
    for i in range(iters):
        X=1/2*(X+n/X)
    return X

#the reason that it was wrong was because you didn't return any value
#the return statment brings back the value to where the function was called

def testmySQRT():
    mySQRT(16,100)
    print(mySQRT(16,100))
    x= mySQRT(16,100)
    print(x)
    y= mySQRT(16,100) * mySQRT (25,100)
    print(y)
#testmySQRT()
#an error returns because the value returned is considered a string

#2
def lab3_2():
    s= 'in the loop'
    #a
    for i in range(3):
        print(s)
    print('')
    #b
    for i in range(2,7,2):
        print(s)
    print('')
    #c
    for i in range(15,0,-5):
        print(s)
    print('')

    #d
    for i in range(-3,0,1):
        print(s)
    print('')
    #e
    for i in range(9,0,-3):
        print(s)
    print('')
#lab3_2()

#3
def schoolDaze_if(age):
    if(age<=0):
         print("You are not alive")
    if(age>=1 and age<=3):
        print("Nursery")
    if(age>=4 and age<=5):
        print("Preschool")
    if(age>=6 and age<=11):
        print("Elementary")
    if(age>=12 and age<=13):
        print("Middle School")
    if(age>=14 and age<=18):
        print("High School(aka death)")
    if (age>18):
        print("YAYA NO SCHOOOOOOL")
#schoolDaze_if(-15)

#4
def schoolDaze_nest(age):
    if(age<=0):
         print("You are not alive")
    else:
        if(age>=1 and age<=3):
            print("Nursery")
        else:
            if(age<=5):
                    print("Preschool")
            else:
                if(age<=11):
                    print("Elementary")
                else:
                    if(age<=13):
                        print("Middle School")
                    else:
                        if(age<=18):
                            print("High School(aka death)")
                        else:
                            if (age>18):
                                print("YAYA NO SCHOOOOOOL")

#schoolDaze_nest(7)

#5
def schoolDaze_elif(age):
    if(age<=0):
         print("You are not alive")
    elif(age>=1 and age<=3):
        print("Nursery")
    elif(age<=5):
        print("Preschool")
    elif(age<=11):
        print("Elementary")
    elif(age<=13):
        print("Middle School")
    elif(age<=18):
        print("High School(aka death)")
    elif (age>18):
        print("YAYA NO SCHOOOOOOL")
#schoolDaze_elif(22)



#6
def PRS(p1,p2):
    
    if(p1=='rock'):
        if(p2=="paper"):
            print('paper covers rock')
        elif(p2=="scissors"):
            print('rock dulls scissors')
        elif(p2=="rock"):
            print('tie')
        else:
            print("invalid")

    elif(p1=='paper'):
        if(p2=="rock"):
            print('paper covers rock')
        elif(p2=="scissors"):
            print('scissors cuts paper')
        elif(p2=="paper"):
            print('tie')
        else:
            print("invalid")

    elif(p1=='scissors'):
        if(p2=="paper"):
            print('scissors cuts paper')
        elif(p2=="rock"):
            print('rock dulls scissors')
        elif(p2=="scissors"):
            print('tie')
        else:
            print("invalid")
    else:
         print("invalid")


#PRS('rock',"p2")
#PRS('rock',"rock")
#PRS('scissors',"paper")

#7
def testPRS():
    list=['rock', 'paper','scissors','hi']
    for i in list:
        for n in list:
            PRS(i,n)
#testPRS()

#8
def calcAutoPremium(age,numDoor,gender):

    premium=0
    if age<21:
        if numDoor==2:
            print('High Risk')
            if(gender=="female"):
                premium=2500*(2/3)
            if(gender=="male"):
                premium=2500*2
            else:
                print("No Gender entered")
        else:
            print("Semi-High Risk")
            if(gender=="female"):
                premium=1900*(2/3)
            if(gender=="male"):
                premium=1900*2
            else:
                print("No Gender entered")
    else:
        if numDoor==2:
            print('Medium Risk')
            premium=1500
        else:
            print("Low Risk")
            premium=800
    monthlyPayment= premium/12.0
    return monthlyPayment


#9
def testAutoPremium():
    gender=['female', 'male','hi']
    for i in gender:
        for n in range(1,4,2):
            for a in range(20,23):
                print(calcAutoPremium(a,n,i))


testAutoPremium()













