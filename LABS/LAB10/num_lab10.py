#Heather Dalton
#11/05/2019

manyLists=[[2,1,3,1,3,2],[3,4,5,6,7],[9,4,2,7,8,6,3,1,9],[12,3,2,1,2]]
moreLists = [[5,4,6],[2,1,3,9],[6,7,5,8,4]]
moreListsB = [[5,5,4,6,5,6], [6,7,5,8,4],[2,1,3,9,8]]
import random

#1
def commonLists(lst1,lst2):
    same=0
    for k in range(len(lst1)):
        for i in range(len(lst2)):
            if lst1[k] == lst2[i]:
                same+=1
    return same
        
##print(commonLists(moreLists, moreListsB))
##print(commonLists(moreLists, moreLists))
##print(commonLists(manyLists, moreLists))
##print("")

#2
def scrambleEachList(aListOfLists):
    newL=[]
    y=len(aListOfLists)
    for k in aListOfLists:
        y=len(k)
        aList=k[:]
        for i in range(len(aList)):
            rand=random.randrange(0,y)
            x=aList.pop(i)
            aList.insert(rand,x)
            y-=1
        newL.append(aList)
    return newL

##print(moreLists)
##print(scrambleEachList(moreLists))
##print("")




#3
def aListOfListsDupes(aListOfLists):
    full=[]
    for i in aListOfLists:
        alist=i[:]
        repeated=[]
        notRep=[]
        for k in range(len(alist)):
            if alist[k] not in notRep:
                notRep.append(alist[k])
            elif alist[k] not in repeated:
                repeated.append(alist[k])
        full.append(repeated)
    return full
#print(aListOfListsDupes(moreListsB))      

#4
def sumTheListPositions(lol1,lol2):
    lstSum=[]
    for i in range(len(lol1)):
        lst1=[]
        if len(lol1[i])<=len(lol2[i]):
            for j in range(len(lol2[i])):
                if j >= len(lol1[i]):
                    lst1.append(lol2[i][j])
                else:
                    add= lol1[i][j]+lol2[i][j]
                    lst1.append(add)
                    
            lstSum.append(lst1)
        else:
            for j in range(len(lol1[i])):
                if j>= len(lol2[i]):
                    lst1.append(lol1[i][j])
                else:
                    add= lol1[i][j]+lol2[i][j]
                    lst1.append(add)
                    
            lstSum.append(lst1)
    return lstSum
            
    
##print(sumTheListPositions([[],[]],[[3,4,2],[6,9]]))
##print(sumTheListPositions([[7,8],[]],[[3,4,2],[6,9]]))


#Dictionaries
d1={"Bob":[5,4,3,2,1,2],"Sue":[2,3,1,4,4,3,2],"Jill":[6,5,6,4,3,1]}
d2={"Joe":[3,1,4,4],"Sally":[5,1,3,7],"Bob":[2,2,3,3,2]}

#5
def sortCounts(aDictionary):
    for i in aDictionary:
        i=aDictionary[i].sort()
    return aDictionary
##print(sortCounts(d1))

#6
def lookupD(aDictionary):
    sOc= input("Enter a state or capitol ('QUIT' to quit)=> ")
    while sOc!= "QUIT":
        if sOc in aDictionary:
            print(aDictionary[sOc])
        elif sOc in aDictionary.values():
            for key in aDictionary:
                if aDictionary[key]==sOc:
                    print(key)
        else:
            print("Not Found")
        sOc= input("Enter a state or capitol ('QUIT' to quit)=> ")


lookupD({"Alaska":"Juneau","Idaho":"Boise","Ohio":"Columbus"})


classGrades={"COS120":{"Bob":[98,100,100,88],
                       "Sue":[100,88,100,100],
                       "Jill":[100,100,100,100]},
             "ENG110":{"Sue":[100,100,100,100,88],
                       "Mary":[88,90,88,90,88],"John":[100,100,100,100,100],
                       "Joe":[90,90,70,70,80]},
             "BIB231":{"Bob":[98,100,100,88],"Sue":[88,88,88,88],
                       "Jill":[100,100,100,100]}}

#7
def calcGrades(classD):
    for key in classD:
        print(key)
        keys=(classD[key].keys())
        values=(classD[key].values())
        for i in keys:
            total=0
            for k in range(len(classD[key][i])):
                total+=classD[key][i][k]
            total= total/(len(classD[key][i]))
            if total>=90:
                total='A'
            elif total>=80:
                total='B'
            elif total>=70:
                total='C'
            elif total>=60:
                total='D'
            else:
                total='F'
            print(i.rjust(12),total)

calcGrades(classGrades)               

#8
def convertD(classd):
    newd={}
    for key in classd:
        for name in classd[key]:
            if name not in newd:
                newd[name]={}
                newd[name][key]= classd[key][name]
            else:
                newd[name][key]= classd[key][name]
    print(newd)

convertD(classGrades)

        
