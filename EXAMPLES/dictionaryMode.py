#10/09/2019
x=[5,2,3,1,3,4,2,5]

def ModeByDictionary(lst):
    modeList=[]
    countd={}
    for item in lst:
        if item not in countd:
            countd[item]=1
        else:
            countd[item]+=1
    lstV=list(countd.values())
    maxVal=max(lstV)
    for key in countd:
        if countd[key]==maxV:
            modeList.append(key)
    return modeList
