#Heather Dalton
#10/08/2019
import random
#1
def showListFunctions(myClasses):
    print(myClasses[2:])
    
    classess= ["COS 102","ENG 110"]
    for i in classess:
        if(i not in myClasses):
            print(i+" is NOT in list already")
            myClasses.append(classess)
            print (myClasses)
        else:
            print(i+" is in list already")
            print (myClasses)

    print(myClasses[-2])
    print(len(myClasses))
    print(myClasses+myClasses)

    for i in range(len(myClasses)):
        if myClasses[i]== "ENG 110":
            print("ENG 110 found at " +str(i))
        else:
            print("not found")
        
cls=["COS 120", "ENG 110", "SYS 100", "BIB 110"]
#showListFunctions(cls)


#2
def showTimeForClass(myClasses, times):
    x=input("Enter a course designation =>")
    for i in range(len(myClasses)):
        if myClasses[i]==x:
            return times[i]
    return False
            
        
t=[1100,800,1300,1500]
c=["COS 120", "ENG 110", "SYS 100", "BIB 110"]
      
#3
def showTimeForClass2(myClasses,times):
    combined= myClasses+times
    x=len(combined)//2
    print (combined[:x])
    newC=combined[:x]
    newT=combined[x:]
    print(showTimeForClass(newC,newT))
    
#showTimeForClass2(c,t) #NUmber 2 is imbeded to 3

#4
def demoListMethods(aList):
    print("Appended")
    aList.append("IAS 110")
    print(aList)
    print("")

    print("Insert")
    aList.insert(-1,"SYS 120")
    print(aList)
    print("")

    print("Pop")
    aList.pop(-3)
    print(aList)
    print("")

    print("Sort")
    aList.sort()
    print(aList)
    print("")

    print("Reverse")
    aList.reverse()
    print(aList)
    print("")

    print("Index")
    print(aList[2])
    print("")

    print("Count")
    print(aList.count("COS 120"))
    print("")

    print("Remove")
    aList.remove("SYS 120")
    print(aList)
    print("")
    
#demoListMethods(["COS 120", "ENG 110", "SYS 100", "BIB 110"])


#5
lists=[1,2,3,4]

def reverseList1(aList):
    reverse=[]
    for i in range(len(aList)-1,-1,-1):
        reverse.append(aList[i])
    return reverse

def reverseList2(aList):
    reverse=[]
    for i in range(len(aList)):
        reverse.insert(0,aList[i])
    return reverse
    
def reverseList3(aList):
    length = len(aList)
    s = length

    new_list = [None]*length

    for item in aList:
        s = s - 1
        new_list[s] = item
    return new_list

"""print(reverseList1(lists))
print(reverseList2(lists))
print(reverseList3(lists))
"""

#6
def shuffleToNewList(alist):
    print(alist)
    newL=alist[:]
    newL.sort()
    for i in range(len(newL)):
        rand=random.randrange(0,len(newL))
        x=newL.pop(i)
        newL.insert(rand,x)
    return newL
        
print(shuffleToNewList([1,2,3,4,5,6,7,8,9,0]))
print("")
#7
def shuffleInList(alist):
    print(alist)
    y=len(alist)
    for i in range(len(alist)):
        rand=random.randrange(0,y)
        x=alist.pop(i)
        alist.insert(rand,x)
        y-=1
    return alist

print(shuffleInList([1,2,3,4,5,6,7,8,9,0]))

