#Heather Dalton
#09/20/2019

"""Write a 3 rail transposition encrytption algorithm,
and a correspnding decryption algorithm.  Implement these two
algorithms in their own function.  Now write a testing function that
demonstrates your algorithms work for all interesting cases!"""

def Scramble3Encrypt(plainText):
    dzero=""
    done=""
    dtwo=""
    charCount=0
    for ch in plainText:
        if charCount%3==0:
            dzero= dzero+ ch
        elif charCount%3==1:
            done= done+ ch
        elif charCount%3==2:
            dtwo= dtwo+ ch
        charCount=charCount+1
    cipherText= dzero+done+dtwo
    return cipherText

def Scramble3Decrypt(cypherText):
    plaintext=""
    third=(len(cypherText)//3)

    if(len(cypherText)%3==2):
        dzero=cypherText[:third+1]
        done=cypherText[third+1:third*3]
        dtwo=cypherText[third*3:]
    elif(len(cypherText)%3==1):
        dzero=cypherText[:third+1]
        done=cypherText[third+1:(third*2)+1]
        dtwo=cypherText[(third*2)+1:]
    else:
        dzero=cypherText[:third]
        done=cypherText[third:(third*2)]
        dtwo=cypherText[(third*2):]
    #print(len(cypherText))
    #print(dzero)
    #print(done)
    #print(dtwo)
    #print("")


    if(len(cypherText)%3==2):
        for i in range(third):
                plaintext= plaintext+dzero[i]+done[i]+dtwo[i]
        plaintext=plaintext+dzero[-1]+done[-1]

    else:
        for i in range(third):
            plaintext= plaintext+dzero[i]+done[i]+dtwo[i]
        
        if(len(cypherText)%3==1):
            plaintext=plaintext+dzero[-1]
        if(len(cypherText)%3==0):
            if(len(cypherText)%3!=0):
                plaintext=plaintext+dzero[-1]
    
    return plaintext


print(Scramble3Decrypt(Scramble3Encrypt("Hi!"))) #length=3
print(Scramble3Decrypt(Scramble3Encrypt("Hi fred!"))) #length=8
print(Scramble3Decrypt(Scramble3Encrypt("Hello world!")))#length=12
print(Scramble3Decrypt(Scramble3Encrypt("Hello world! my name is heather")))#length=31
print(Scramble3Decrypt(Scramble3Encrypt("What is your name?")))#length=18

"""So far this code only decrypts for values != 2,5,14,17,20,23,26,32
(only a few that I tested)"""



