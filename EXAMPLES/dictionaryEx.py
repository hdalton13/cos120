#10/09/2019

#defining a dictionary :D
d={'tim': 100, 'Sue': 99, 'Bob': 87}

#Add key values
d['Mary']=95
print((d))

#Remove Bob key values
del d['Bob']
print(d)

#Update Sue's score
d['Sue']=100
print((d))

#make tim a capital Tim
d['Tim']=d['tim']
del d['tim']
print(d)

#Extract List of scores
scores=list(d.values())
print(scores)

#Extract a list of the keys
keys=list(d.keys())
print(keys)

#for loop
for k in d:
    print(k)
print('')


"""Write a function that will accept a
dictionary as an argument and print the
keys in alphabetical order with the
corresponding value following each key
on the same line (key  value, one per line)
"""
def showKeysAndValues(d):
    keyList=list(d.keys())
    keyList.sort()
    for key in keyList:
        print(key,d[key])
        
x={"joe":29, 'abe':12,'bert':16,'mary':12}
#showKeysAndValues(x)


'''Write a function that will accept a dictionary
as an argument and a value as an argument and return
a list of all keys that are paired with that value '''
def valuesPairWithKey(d,values):
    keyList=[]
    for key in d:
        if d[key]==values:
            keyList.append(key)
    return keyList
    
print(valuesPairWithKey(x,12))


