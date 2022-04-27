x=[21,3,12,6,1,5,21,3,77,2,9,8,5,56]
def sparceListMode(lst):
    maxVal=max(lst)
    sparceList=[]
    modeList=[]
    for i in range(maxVal+1):
        sparceList.append(0)
    for num in lst:
        sparceList[num]+=1
    maxCount=max(sparceList)
    for i in range(len(sparceList)):
        if sparceList[i]==maxCount:
            modeList.append(i)
    return modeList
print(sparceListMode(x))
