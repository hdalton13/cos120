#Heather Dalton
#10/15/2019

w=[83,99,2,3,1,7,54,1]
x=[23,12,67,5,4,11,2,84,12,16]
y={"staplers":2,"pencils":45,"erasers":12,"paper clips":200, "pens":84,"markers":12}
z={23012:2,77321:5,32332:234,77656:16,21321:802,99876:3}

"""
#1
print("List:")
for i in x:
    print (i)
print("")

#2
print("All of Dictionary:")
print(y.items())
print("")

#3
print("Dictionary Sort Key")
def showSortKeys(d):
    keyList=list(d.keys())
    keyList.sort()
    for key in keyList:
        print(key,d[key])
showSortKeys(y)     
print("")



#4
print("Dictionary Sort Items")
def showSortValues(d):
    old=list(d.values())
    #print(old)
    key=list(d.keys())
    #print(key)
    new=list(d.values())
    #new.sort()
    print(new)
    for ch in range(len(new)):
        idx= old.index(new[ch])
        print(key[idx],":",new[ch])
              
showSortValues(y)      
print("")


#5
print("Add to List")
x= int(input ("Value"))
w.append(x)
print(w)
print("")

#6
print("Add to Dictionary")
n= input("Key name")
x= int(input ("Value"))
y[n]=x
print((y))
print("")


#7
def inDictionary(x):
    look= input("Key Name")
    if look in x:
        return x.get(look)
    else:
        return "No such value"
print(inDictionary(y))


#8
def inList(lst,x):
    for i in lst:
        if i==x:
            return True
    return False

print(inList(w,99))
print(inList(w,10))


w=[83,99,2,3,1,7,54,1]
#9
def ascendingSort(lst):
    newLst=lst[:]
    new=[]
    least=1
    for i in range(len(lst)):
        least=newLst.index(min(newLst))
        new.append(min(newLst))
        newLst.pop(least)
    print(new)
        
print(w)
ascendingSort(w)
print("")

list1=[1,2,3]
list2=[4,5,6]

#10
def twoAscending(lst1, lst2):
    newLst=[]
    i=0
    k=0
    while(len(lst1)>i and len(lst2)>k):
        if(lst1[i]<lst2[k]):
            newLst.append(lst1[i])
            i+=1

        elif((lst1[i]>lst2[k])):
            newLst.append(lst2[k])
            k+=1
        if(i==len(lst1)):
            newLst+=(lst2[k:])
            break
        if(k==len(lst2)):
            newLst+=(lst2[i:])
            break

    return newLst

            
print(twoAscending(list1,list2))
print("")

#11
def useTen():
    num=[10,12,14,16,18]
    other=[11,13,15,17,19]
    num.sort()
    other.sort()
    return twoAscending(num,other)
    
print(useTen())
"""

#12
import turtle
d=[[39,2],[16,5],[14, 99],[2,1],[28,12],[12,28],[20,50],[38,77]]
    
def turtleDots(lst):
    wn = turtle.Screen()
    alex=turtle.Turtle()
    max_X=max([sublist[0] for sublist in lst])
    max_Y=max([sublist[1] for sublist in lst])
    min_x=min([sublist[0] for sublist in lst])
    min_y=min([sublist[1] for sublist in lst])
    wn.setworldcoordinates(min_x-10, min_y-10, max_X+10, max_Y+10)

    alex.penup()
    alex.goto(0,0)
    alex.pendown()
    alex.forward(100)
    alex.backward(200)
    alex.forward(100)
    alex.left(90)
    alex.forward(120)
    alex.backward(240)
    alex.forward(120)

    for i in range(len(lst)):
        alex.penup()
        alex.goto(lst[i][0],lst[i][1])
        alex.dot()

        
turtleDots(d)
 
#13
#Still don't really understand
"""
If the dictionary contains replicate values, return an empty dictionary,
otherwise,return a new dictionary whose values are now the keys and whose
keys are the values. 
"""
def createNewValuesD(dic):
    new={}
    sec={}
    for i in dic:
        if dic[i] not in new:
            new[dic[i]]=i
        else:
            return backup
    return new
die={"a":5, "b":12, "k":13}
print(createNewValuesD(die))

#14
#Still don't really understand
hom=[["pie","pi"],["c","see","sea","si"]]
def homonyms(lst):
    new={}
    for i in lst:
        for k in i:
            idx= i.index(k)
            copy=i[:]
            copy.pop(idx)
            new[k]=copy
    return new
            
print(homonyms(hom))






































