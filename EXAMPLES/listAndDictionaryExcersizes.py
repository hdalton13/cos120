#10/16/2019

#1 create a new list so that only the repeated values r repeated once
def unionLst(lst1,lst2):
    new=[]
    for i in lst1:
        if(i not in new):
            new.append(i)
    for k in lst2:
        if(i not in new):
            new.append(i)
    return new

def unionLst2(lst1,lst2):
    new=[]
    for i in lst1+lst2:
        if(i not in new):
            new.append(i)
    return new

#2 find all of the values that repeat in the two lists
def intersect(lst1,lst2):
    new=[]
    for i in lst1:
        if(i in lst2 and i not in new):
            new.append(i)
    return new

da={1:5,5:2,4:6,8:3,2:9}
db={8:77,9:88,7:66,1:11}

#3 replace the value of d1 with the value that is equal to the same key in d2
def dreplaceD(d1,d2):
    for key in d1:
        if key in d2:
            d1[key]=d2[key]
    return d1
"""print(dreplaceD(da,db))"""

#4 swap the values from each list that have the same keys
def dSwapD(d1,d2):
    for key in d1:
        if key in d2:
            temp=d1[key]
            d1[key]=d2[key]
            d2[key]=temp
    print(d1)
    print(d2)
"""dSwapD(da,db)"""

a={'bob':12, 'tom':33,"sue":98,'george':15}
b={'larry':19,'george':21,'bob':1}

#5 look at the keys and create a new dic with
    #elements that are not repeated within both origianal dictionaries
def dDiffDO(dic1,dic2):
    newD={}
    for i in dic1:
        if i not in dic2:
            newD[i]=dic1[i]
    for i in dic2:
        if i not in dic1:
            newD[i]=dic2[i]
    return newD

"""print(dDiffDO(a,b))"""

#6 add all the values for the common Keys
def dSumD(d1,d2):
    newD={}
    for i in d1:
        if i in d2:
            newD[i]= d1[i]+d2[i]
    return newD
"""print(dSumD(a,b))"""















