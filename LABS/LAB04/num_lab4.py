#Heather Dalton
#09/24/2019

#1
def showASCII(bob):
    for ch in range(len(bob)):
        print(bob[ch]+"="+ str(ord(bob[ch])))

#showASCII("ABCD")


#2
def printASCIIRange(start, stop):
    string=""
    for ch in range(start,stop+1):
        print (str(ch)+"= "+ str(chr(ch)))

#printASCIIRange(65, 69)


#3
def reverseString(string):
    new=""
    for i in range(len(string)-1,-1,-1):
        new= new + string[i]
    return new

#print(reverseString("hello"))

#4
def changeCase(chara):
    if (ord(chara)<=90) and (ord(chara)>=65):
        num= int(ord(chara))+32
        return(chr(num))
    elif (ord(chara)<=122) and (ord(chara)>=97):
        num= int(ord(chara))-32
        return(chr(num))
    else:
        return chara
#print(changeCase("z"))
#print(changeCase("Z"))
#print(changeCase("&"))

#5
def upperCase(string):
    upper=""
    for ch in string:
        if(ord(ch)<=122) and (ord(ch)>=97):
            new= changeCase(ch)
            lower= lower+new
        else:

            lower= lower+ch
    return upper

def lowerCase(string):
    lower=""
    for ch in string:
        if(ord(ch)<=90) and (ord(ch)>=65):
            new= changeCase(ch)
            lower= lower+new
        else:
            lower= lower+ch
    return lower


#print(lowerCase("123 HeLlo BOB #$% abcD"))

#6
def formateLongDate(date):
    month= date[:2]
    day= int(date[3:5])
    year= date[6:]
    date=""
#
    if(month=="01"):
        date= "January"
    elif(month=="02"):
        date= "Febuary"
    elif(month=="03"):
        date= "March"
    elif(month=="04"):
        date= "April"
    elif(month=="05"):
        date= "May"
    elif(month=="06"):
        date= "June"
    elif(month=="07"):
        date= "July"
    elif(month=="08"):
        date= "August"
    elif(month=="09"):
        date= "September"
    elif(month=="10"):
        date= "October"
    elif(month=="11"):
        date= "November"
    elif(month=="12"):
        date= "December"
    else:
        return "Invalid Month"
  
    date= date +" "+str(day)+", "


    date= date+ "20"+year
    return date
#print(formateLongDate("09/05/99"))


#7
def stringToASCIICodesString(add):
    encrypt=""
    for ch in add:
        encrypt+= "0"+ str(ord(ch))
    return encrypt

#print(stringToASCIICodesString("BAD"))

"""if(add[ch+3]!=0):
                num+= str(add[ch+3])
                num= int(num)
                encrypt= encrypt + chr(num)
            else:
                """
#8
def ASCIICodesStringToString(add):
    encrypt=""
    for ch in range(0,len(add),3):
        if(add[ch]=="0"):
            num= str(add[ch+1])+str(add[ch+2])
        if(add[ch]!=0):
            num = str(add[ch])+ str(add[ch+1])+str(add[ch+2])
            num= int(num)
            encrypt= encrypt + chr(num)
            
        
    return encrypt

#print(ASCIICodesStringToString("120065068"))

#9

def transposition2RailEncrypt(plainText): #2 rail trans. encryption
    evenChars = ""    
    oddChars = ""    
    for i in range (len(plainText)):
        if i % 2 == 0:                            
            evenChars = evenChars + plainText[i]
        else:            
            oddChars = oddChars + plainText[i]
    cipherText = oddChars + evenChars    
    return cipherText

#print(transposition2RailEncrypt("Hello Bob!"))


def myEncrypt(plainText):
    en_3= plainText
    for i in range(3):
        en_3= transposition2RailEncrypt(en_3)
    return en_3

print(myEncrypt("Hello Bob!"))





























