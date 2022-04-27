#11/08/2019

"""Write a pyhton funtion subListIndex to return the index of the first
occurence of a sublist or -1 if it doesn't exist in the main list"""

def subListIndex(lst1,lst2):
    if len(lst2)<len(lst1) or len(lst1)==0 or len(lst2)==0:
        return -1
    for index in range(len(lst2)):
        if lst1==lst2[index:index+len(lst1)]:
            return index
    else:
        return -1

print(subListIndex([4,1,7],[1,2,3,4,1,7,2]))


"""Write a python function circularIdentity to return
wheather two lists are circularly identical"""

def circularIdentity(lstA,lstB):
    if len(lstA)!=len(lstB):
        return False
    for i in range(len(lstA)):
        lstA.append(lstA.pop(0))
        if lstA==lstB:
            return True
    return False
print("")
print(circularIdentity([1,2,3],[3,1,2]))
print(circularIdentity([1,2,3],[2,3,1]))
print(circularIdentity([1,2,3],[3,2,1]))


'''Write a python function subset to return whether
the first list is a subset of the second(item order is not critical)'''

def subset(sub,lst):
    for item in sub:
        if item not in lst:
            return False
    return True
print("")
print(subset([1,2,3],[3,1,2]))
print(subset([1,2,3,5],[3,1,2,4]))
