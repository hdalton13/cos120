
lst=[[2,1],[1,3,2],[4,1,5],[2,4,6,8],[1,5]]
remove=[2,1,4]

def removeFromList(listOfLists, forbNumLst):
    lOl=[]
    for i in listOfLists:
        lst=[]
        for k in range(len(i)):
            if i[k] not in forbNumLst:
                lst.append(i[k])
        lOl.append(lst)
    print(lOl)
removeFromList(lst, remove)
