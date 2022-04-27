lst=[3,2,1,7,3,7,4,7,2,5,7,5,5,3,1,2,7,1]

def listModes(alist):
    modeList=[0]
    for item in alist:
        if alist.count(modeList[-1])<alist.count(item):
            modeList =[item]
        elif alist.count(modeList[-1])==alist.count(item) and item not in modeList :
            modeList.append(item)
    return(modeList)

print(listModes(lst))

"""How can you improve this"""
