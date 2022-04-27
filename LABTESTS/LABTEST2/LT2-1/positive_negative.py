#Heather Dalton
#Lab Test
#Statrted 8:05

def positiveAndNegative(lst):
    positive=[]
    negative=[]
    zeros=0
    for i in lst:
        if i==0:
            zeros+=1
        if i <0:
            negative.append(i)
        if i >0:
            positive.append(i)
    print("+ =>",positive)
    print("- =>", negative)
    print("0's =>", zeros)
positiveAndNegative([3,2,6,7,-2,0,1,-5,0,0,7,-1])
