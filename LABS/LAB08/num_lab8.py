#10/22/2019
#Heather Dalton
##67

#1
def writeRainfall():
      rainfile = open("rainfall.txt","r")
      outfile = open("rainfallfmt.txt","w")
      for aline in rainfile:
            values = aline.split()
            inches = float(values[1])
            outfile.write("%+25s %4.1f \n" %(values[0],inches))
      rainfile.close()
      outfile.close()

#writeRainfall()

#2
def convertFer_Cel():
      outfile = open("tempconv.txt","w")
      outfile.write("%+10s %+10s \n" %("Fahrenheit","Celsius"))
      for i in range(-300,213):
            outfile.write("%+10.3f %10.3f \n" %(i,((i-31)*5)/9))
      outfile.close

#convertFer_Cel()

#3
"""The readlines will include all of the values that was not already
called. Ex) everything exept the first two calls of readline"""
def logic1():
      infile = open("rainfall.txt" , "r")
      aline = infile.readline()
      print(aline)
      aline = infile.readline()
      print(aline)
      linelist = infile.readlines()
      print(linelist)
      infile.close()
logic1()
#print('')

#4
"""Just calling readlines will read all of the lines that is there"""
def logic2():
      infile = open("rainfall.txt" , "r")
      linelist = infile.readlines()
      print(linelist)
      infile.close()
#logic2()

#5
def psalmUpper():
      psalm = open("psalm112.txt","r")
      outfile = open("psalm112Upper.txt","w")

      for aline in psalm:
            outfile.write(aline.upper())

      psalm.close()
      outfile.close()
#psalmUpper()

#6
def countPsalm():
    psalm = open("psalm112.txt","r")
    lines=0
    word=0
    char=0

    for aline in psalm:
        for i in aline:
            char+=1
        lines+=1
        word+=len(aline.split())
    
    print('Lines=',lines)
    print('Words=',word)
    print('Charactuers=',char)
    psalm.close()
    
#countPsalm()

#7
def pirateConcord(filename):
    pirate = open(filename,"r")
    outfile=open("concord.txt","w")
    alist=[]
    dic={}
    #Splits each word
    for i in pirate:
        alist.append(i.split())

    #finds repeated words
    for j in range(6):
        for word in alist[j]:
            if (word in alist[j]) and word not in dic:
                dic[word]=[]
                dic[word].append(j+1)
            elif (j+1) in dic[word] and word in dic:
                pass
            else:
                dic[word].append(j+1)
    for ch in dic:
        outfile.write("%+15s %s \n" %(ch,str(dic[ch])))


        
    outfile.close()    
    pirate.close()

pirateConcord("forPirateConversion.txt")


#8
def pirateConcordSort(filename):
    pirate = open(filename,"r")
    outfile=open("concord2.txt","w")
    alist=[]
    dic={}
    #Splits each word
    for i in pirate:
        alist.append(i.split())

    #finds repeated words
    for j in range(6):
        for word in alist[j]:
            if (word in alist[j]) and word not in dic:
                dic[word]=[]
                dic[word].append(j+1)
            elif (j+1) in dic[word] and word in dic:
                pass
            else:
                dic[word].append(j+1)
    

    keyList=list(dic.keys())
    keyList.sort()

    for ch in keyList:
        outfile.write("%+15s %s \n" %(ch,str(dic[ch])))
    
    outfile.close()    
    pirate.close()

pirateConcordSort("forPirateConversion.txt")
















      
