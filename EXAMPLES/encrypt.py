#09/18-20/2019
#Heather Dalton

#Odd even character
def Scramble2Encrypt(plainText):
    evenCh=""
    oddzChars=""
    for evenIndex in range(0,len(plainText),2):
        evenCh= evenCh+ plainText[evenIndex]
    for oddIndex in range(1,len(plainText),2):
        oddzChars= oddzChars + plainText[oddIndex]
    return oddzChars + evenCh

print(Scramble2Encrypt("Hello Bob!"))

def sliceSome(aString):
    if len(aString)>10:
        return aString[2:5]
    else:
        return aString

"""Write a slice for a string of any
length that will return the first half of the string.
If the string contains an odd number of characters, let the first half
contain the longer string"""

def firstHalf(aString):
    if len(aString)%2==0:
        return aString[0:len(aString)//2+1]
    else:
        return aString[0:len(aString)//2]

#No Spaces
def stripSpaces(myString):
    nspace=""
    for ch in myString:
        if ch!= " ":
            nspace= nspace+ ch
    return nspace
print(stripSpaces('I did my hw'))

#Substitution Cipher
def substitutionCipher(plaintext,key);
    cipher=""
    alphabate= abcdefghijklmnopqrstuvwxyz
    key= 
    for ch in plaintext:
        index= alphabate.find(ch)
        cipher= cipher+ key[index]
    return cipher
print(substitutionCipher(plaintext,key))





    
