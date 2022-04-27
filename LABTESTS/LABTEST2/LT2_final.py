#Heather Dalton
#Lab Test
#See Dr. White==> Allowed to break up time and have up to 6hrs to complete
#Started 8:05-10:50 paused
#Started 11:40- 2:00 finished

#1
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

#2
lst=[[2,1],[1,3,2],[4,1,5],[2,4,6,8],[1,5]]
remove=[2,1,4]

def removeFromList(listOfLists, forbNumLst):
    lOl=[]
    for i in listOfLists:
        lst=[]
        for k in range(len(i)):
            if i[k] not in forbNumLst:
                lst.append(i[k])
        lOl.append(lst)
    print(lOl)
removeFromList(lst, remove)

#3
stems=['love','walk','count','hunt']
suffex=['counts','hunter','huntress','loved','loves','loving','counter','hunted','counted','loveless']

def makeStemsD(listOfStems, suffexedWords):
    newD={}
    lst=[]
    for stems in listOfStems:
        for suf in suffexedWords:
            if stems[:3]==suf[:3]:
                lst.append(suf)
        newD[stems]=lst
        lst=[]
    print(newD)
makeStemsD(stems, suffex)

flightsD={"Delta":{1102:[["IND",1850],["MDW",1955]],
                   1096:[["PHX",900],["MDW",1255]],
                   1445:[["ATL",1135],["LAX",1810]],
                   1776:[["PHL",1350],["RAP",1610]],
                   1226:[["PHX",950],["MDW",1345]],
                   1885:[["ATL",1305],["LAX",2000]],
                   1009:[["MDW",1850],["IND",1955]],
                   9001:[["MDW",2145],["IND",2255]]},
          "Southwestern":{1111:[["SAT",430],["MDW",825]],
                          1350:[["MDW",1350],["IND",1455]],
                          4335:[["PHX",450],["MDW",745]],
                          1102:[["MDW",1100],["PHX",1450]]},
          "American":{7765:[["IND",1850],["CHA",2105]],
                   2133:[["BNA",900],["IND",1115]],
                   3321:[["HOU",1335],["ATL",1615]],
                   2100:[["BNA",900],["IND",1115]],
                   4311:[["HOU",905],["ATL",1255]],
                   5577:[["ATL",1100],["HOU",1350]],
                   1102:[["BNA",1100],["HOU",1450]]}}
#4
def reportFlightsFromToBefore(fd,depCDity,arrCity,latest):
    for aK in fd:
        print(aK)
        time="am"
        timed="am"

        for fK in fd[aK]:
            arrTime=fd[aK][fK][0][1]
            #print(fd[aK][fK][1][1])
            if arrTime>1200:
                arrTime=arrTime-1200
                time="pm"

            dTime=fd[aK][fK][1][1]
            if dTime>1200:
                dTime=dTime-1200
                timed="pm"
            if fd[aK][fK][0][0]==depCDity and fd[aK][fK][1][0]==arrCity and fd[aK][fK][1][1]<=latest:
               print(str(fK).rjust(5), str(fd[aK][fK][0][0]).rjust(4),str(arrTime).rjust(4)+time,str(fd[aK][fK][1][0]).rjust(4),str(dTime).rjust(4)+timed)


reportFlightsFromToBefore(flightsD,"MDW","IND",2000)


#5 Started but don't know how to go after the problem and didn't make any progress after one hour
def reportFlightsSameAirlineRoundTrip(fd,depCDity,arrCity):
    print("Round Trip",depCDity,"to",arrCity)
    lst=[]
    for aK in fd:
        #print(aK)
        for fK in fd[aK]:
            first=(fd[aK][fK][0][0])
            second=(fd[aK][fK][1][0])
            
            if ((first==depCDity and (second==arrCity)) or (first==arrCity and (second==depCDity))):
                arrTime=fd[aK][fK][0][1]
                dTime=fd[aK][fK][1][1]
                lst.append([str(aK),str(fK), str(fd[aK][fK][0][0]),str(arrTime),str(fd[aK][fK][1][0]),str(dTime)])
    for i in range(len(lst)-1):
        print (lst[i])
##        if lst[i][2]==lst[i+1][4]:
##            print(lst[i],'=',lst[i+1])


reportFlightsSameAirlineRoundTrip(flightsD,"IND","MDW")
print("")
reportFlightsSameAirlineRoundTrip(flightsD,"PHX","MDW")
print("")
reportFlightsSameAirlineRoundTrip(flightsD,"MDW","PHX")

#6
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def encryptFile(inFile,outFile):
    reading=open(inFile,"r")
    out=open(outFile,"w")
    index=1
    lst=[]
    for aline in reading:
      if index%2==0:
          changed= str(reverse(aline))
          lst.append(changed[1:])
          index+=1
      else:
          newS=""
          line=aline.split()
          for i in line:
              newS+= reverse(i)+" "
          lst.append(newS[:-1])
          index+=1
    for line in lst:
      out.write("%s \n"%line)
    reading.close()
    out.close()

encryptFile("in.txt","out.txt")
