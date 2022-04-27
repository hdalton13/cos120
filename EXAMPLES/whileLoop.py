#10/21/2019

'''Write a loop that will force the user to enter a value between
1 and 10 (loop until they get it right!).  Turn this loop into a
function that allows the user of the function to specify the range
of values they wish to enforce for input.  The function should return
the valid entered value.
'''
def getSpecifiedRange(minN,maxN):
    num=int(input("Enter number between "+str(minN)+" through "+str(maxN)+"=>"))
    while num<minN or num>maxN:
        num= int(input("Enter number between "+str(minN)+" through "+str(maxN)+"=>"))
    return num

#x=getSpecifiedRange(10,1000)

'''Write a function that will randomly select integers in the range
of 0 to 11 inclusive and add the randomly selected integers to a list.
The loop should continue until the value 11 is selected and added, and
then return the list'''
import random
def genRandListEndWith11():
    lst=[]
    num= 0
    while(num!=11):
        num= random.randint(0,11)
        lst.append(num)
    return lst 

#print(genRandListEndWith11())


def genRandList():
    lst=[]
    num= random.randint(0,11)
    while(num!=11):
        lst.append(num)
        num= random.randint(0,11)
    return lst 

#print(genRandListEndWith11())

'''Write a function that will allow a user to enter an unknown number
of integers.  The loop should continue allowing the entry of integers
until they enter ‘quit’.  Return the integers as a list.
'''

def listofEnteredInts():
    lst=[]
    string= input("Enter an integer or quit to quit => ")
    while string != 'quit':
        if string.isdigit():
            lst.append(int(string))
        string= input("Enter an integer or quit to quit => ")
        
    return lst

#print(listofEnteredInts())

'''Write a function that will read line by line through
a file using the readline command
'''
def readwithFile(files):
    inFile=open(files,'r')
    line= inFile.readline()
    while line!= "":
        print(line)
        line= inFile.readline()
readwithFile("test.txt")

