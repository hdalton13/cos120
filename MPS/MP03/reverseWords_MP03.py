#Heather Dalton
#10/2/2019

"""Write a python function that, given a sentence or
collection of words separated by any number of spaces
>=1, will return that sentence or collection of words
in reverse order with at least one separating space
between each word.  The function should work for
sentences of any length, including null strings.
>>> reverseWords("This is a test")
test a is This
"""

def reverseWords(inString):
    string=inString.split()
    #print(string)
    new=""
    for i in range(len(string)-1,-1,-1):
        new=new+string[i]+" "
    new= new[:-1]
    return new


print (reverseWords("This is a test"))
