#Recursion and OOP
#Heather Dalton
#12/3/19
from math import *
#1
def intDivition(num,dem,count):
    #print(num)
    if num-dem<0:
        return count
    else:
        return intDivition((num-dem),dem,count+1)
        
        
#print(intDivition(12,3,0))

#2
def modulus(num,den):
    print(num)
    if num>=den:
        return modulus((num-den),den)
    else:
        return num
        
        
print(modulus(14,3))

#3-11
class Time:
#3
#9 changing self.hrs, self.minutes, self.secs ==> self.__hrs, self.__minutes, self.__secs
    def __init__(self, ihours, iminutes, iseconds): 
        if ihours>0 and ihours<=23:
            self.__hrs=ihours
        else:
            self.__hrs= 0
        if iminutes>0 and iminutes<=59:
            self.__minutes=iminutes
        else:
            self.__minutes= 0
        if iseconds>0 and iseconds<=59:
            self.__secs=iseconds
        else:
            self.__secs= 0
#6        
    def getHr(self):
        return self.__hrs
    def getMin(self):
        return self.__minutes
    def getSec(self):
        return self.__secs
#7
    def setHr(self,ihours):
        if ihours>0 and ihours<=23:
            self.__hrs=ihours
    def setMin(self, iminutes):
        if iminutes>0 and iminutes<=59:
            self.__minutes=iminutes
    def setSec(self, iseconds):
        if iseconds>0 and iseconds<=59:
            self.__secs=iseconds  
#4
    def getTime(self):
        hour=str(self.__hrs)
        minute=str(self.__minutes)
        second= str(self.__secs)
        if int(hour)<10:
            hour= "0"+hour
        
        if int(minute)<10:
            minute= "0"+minute
        if int(second)<10:
            second="0"+second
            
        return  hour+":"+minute+":"+second
#5
    def getCivilianTime(self):
        newTime=self.getTime()
        time="AM"
        newhour= newTime[:2]
        if int(newhour)==12:
            time="PM"
            return str(newhour)+newTime[2:]+time

        if int(newhour)>12:
            newhour= str(24-int(newhour))
            time="PM"
            return str(newhour)+newTime[2:]+time
        return newTime+time
#8
    def incrementTime(self):
        if self.__secs< 59:
            self.__secs+=1
        elif self.__secs==59 and self.__minutes<59:
            self.__secs=0
            self.__minutes+=1
        elif self.__minutes==59 and self.__hrs<23:
            self.__secs=0
            self.__minutes=0
            self.__hrs+=1
        else:
            self.__secs=0
            self.__minutes=0
            self.__hrs=0
#10
    def timeDiff(self,time2):
        if self.__hrs>time2.__hrs:
            h= abs(int(self.__hrs)-int(time2.__hrs))
            m= abs(int(self.__minutes)-int(time2.__minutes))
            s= abs(int(self.__secs)-int(time2.__secs))
        else:
            h= abs(int(time2.__hrs)-int(self.__hrs))
            m= abs(int(time2.__minutes)-int(self.__minutes))
            s= abs(int(time2.__secs)-int(self.__secs))
        return  "Hour=>"+str(h)+" "+"minutes=>"+str(m)+" "+"secs=>"+str(s)
        
    
    def   __str__(self):
        return  "Hour=>"+str(self.__hrs)+" "+"minutes=>"+str(self.__minutes)+" "+"secs=>"+str(self.__secs)


#11
def callTime():
    p4=Time(12,5,55)
    print(p4)
    print(p4.getHr())
    print(p4.getMin())
    print(p4.getSec())
    p4.setHr(4)
    p4.setMin(45)
    p4.setSec(60)
    print(p4)
    p4.incrementTime()
    print(p4)
    p3=Time(13,50,55)
    print(p4.timeDiff(p3))

#callTime()


    
