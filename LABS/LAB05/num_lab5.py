#Heather Dalton
#10/01/2019

#1
def printChars1(str):
    for i in range(len(str)):
        print(str[i])

#2
def printChars2(str):
    for i in str:
        print(i)
#4
def printChars3(str):
    new=""
    for i in range(len(str)):
        new=new+ str[i]
        print(new)
    
#3  
def printChars4(str):
    new=""
    for i in str:
        new=new+ i
        print(new)


#5
def printInReverse1(str):
    new=""
    for i in range(len(str)):
        new=str[i]+new
        print(new)
#6
def printInReverse2(str):
    new=""
    for i in range(len(str)-1,-1,-1):
        new=str[i]+new
        print(new)
    

#7
def length(inString):
    count=0
    for i in inString:
        count+=1
    return count
        

#8
def sliceStr(inString,From,To):
    new=""
    for i in range(From,To):
        new+= inString[i]
    return new

#9
def inString(thisString,targetString):
    string=""
    for i in range(len(thisString)):
        for ch in range(len(targetString)):
            if (thisString[i]==targetString[ch]):
                string= string+ targetString[ch]
                break
    if (string==thisString):
        return True
    else:
        return False
            

#10
def concatenate(firstString,secondString):
    array= [firstString, secondString]
    return "".join(array[:])
    
#11
def find(thisString, inString):
    for i in range(len(inString)):
        if inString[i:i+len(thisString)] == thisString:
            return i
    else:
        return -1

#12
def replace(inString,findString,rplString):
    string=inString.split()
    print(string)
    for i in range(len(string)):
        if(string[i]==findString):
            string[i]= rplString
    new=""
    for i in string:
        new=new+i+" "
    new= new[:-1]
    return new


    
"""
#1-7
printChars1("right")
printChars2("right")
printChars3("right")
printChars4("right")
printInReverse1("hello")
printInReverse2("hello")
print("")
print(length(""))
print(length("1234"))
"""

"""
#8
print(sliceStr("A new start",0,5))
print(sliceStr("A new start",2,5))
print(sliceStr("A new start",2,55))

#9
print(inString("all","none at all"))
print(inString("ally","none at all"))
print(inString("all","all or none at all"))
"""

#print(concatenate("Hello123","1234"))

"""
#11
print(find("all", "all in all"))
print(find("all", "best of all"))
print(find("all", "not in this string"))
"""

#print(replace("I ran ran ran home!", "ran", "walked"))


    
