#10/02/2019

def mean(alist):
    mean = sum(alist)/len(alist)
    return mean


def median(alist):
    copylist = alist[:]     #make a copy using slice operator, why?
    copylist.sort()
    if len(copylist) % 2 == 0:    # even length
        rightIndex = len(copylist)//2
        leftIndex = rightIndex - 1
        median = (copylist[leftIndex ] + copylist[rightIndex ])/2.0
    else:   # odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def mode(alist):
    itemList=[]
    countList=[]
    for thisItem in lst:
        if thisItem not in itemList:
            itemList.append(thisItem)
            countList.append(1)
        else: 
            idx = itemList.index(thisItem)
            countList[idx]=countList[idx]+1
    theMax=max(countList)
    modeList=[]
    for idx in range(len(countList)):
        if countList[idx]==theMax:
            modeList.append(itemList[idx])
    return modeList

"""make two lists
--> uniqueNums
--> countNums
check alist and see if its already in uniqueNum
--> Not
-----> append to unique
-----> append 1 to countNums
-->Yes
---->go to the item in countNum"""
