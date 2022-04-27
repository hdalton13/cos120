stems=['love','walks','count','hunt']
suffex=['counts','hunter','huntress','loved','loves','loving','counter','hunted','counted','loveless']

def makeStemsD(listOfStems, suffexedWords):
    newD={}
    lst=[]
    for stems in listOfStems:
        for suf in suffexedWords:
            if stems[:3]==suf[:3]:
                lst.append(suf)
        newD[stems]=lst
        lst=[]
    print(newD)
    

makeStemsD(stems, suffex)
