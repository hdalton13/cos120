#10/18/2019
flightsD={"Delta":{1102:[["IND",1850],["MDW",1955]],
                   1096:[["PHX",900],["MDW",1255]],
                   1445:[["ATL",1135],["LAX",1810]],
                   1776:[["PHL",1350],["RAP",1610]],
                   1226:[["PHX",950],["MDW",1345]],
                   1885:[["ATL",1305],["LAX",2000]],
                   1009:[["MDW",1850],["IND",1955]],
                   9001:[["MDW",2145],["IND",2255]]},
          "Southwestern":{1111:[["SAT",430],["MDW",825]],
                          2121:[["MDW",430],["SAT",825]],
                          4335:[["PHX",450],["MDW",745]],
                          1102:[["MDW",1100],["PHX",1450]]},
          "American":{7765:[["IND",1850],["CHA",2105]],
                   2133:[["BNA",900],["IND",1115]],
                   3321:[["HOU",1335],["ATL",1615]],
                   2100:[["BNA",900],["IND",1115]],
                   4311:[["HOU",905],["ATL",1255]],
                   5577:[["ATL",1100],["HOU",1350]],
                   1102:[["BNA",1100],["HOU",1450]]}
          }
#^^^this dic is a list of dictionaries of lits of lists^^^

#Names
def namesOfAirlines(fd):    #prints out airline's names
    for key in fd:
        print(key)

def namesOfAirlinesList(fD):
    lstAirlineNames=[]
    for k in fD:
        lstAirlineNames.append(k)
    return lstAirlineNames

def namesOfAirlinesLists(fd):   #returns a list of airline's names
    nl= list(fd.keys())
    nl.sort()
    return nl
"""
namesOfAirlines(flightsD)
print(namesOfAirlinesLists(flightsD))
"""

#print airlines and their flights
def printAandF(fd):
    for airlineNameKey in fd:
        print(airlineNameKey)
        for flightKey in fd[airlineNameKey]:
            print(str(flightKey).rjust(10))
            #                       ^^^^indent flight numbers under airlines
    #Dont be a slug go to the shell if u have a question  -Dr White

def printAandF(fd):
    aKeys=list(fd.keys())
    aKeys.sort()
    for airlineNameKey in aKeys:
        print(airlineNameKey)
        flKeys=list(fd[airlineNameKey].keys())
        flKeys.sort()
        for flightKey in flKeys:
            print(str(flightKey).rjust(10))

'''printAandF(flightsD)'''

#print airline flights arriving at a given airport
def printArivingAT(fd,airport):
    for aK in fd:
        for fK in fd[aK]:
            if fd[aK][fK][1][0]==airport:
    #       airline^  ^airline #  ^arrivels (sub 0 would give the departures)
                depCity=fd[aK][fK][0][0].rjust(4)
                print(aK.rjust(15),str(fK).rjust(5),depCity, str(fd[aK][fK][0][0].rjust(4)))
'''printArivingAT(flightsD,"MDW")'''
                      
#print airline flights arriving at a given airport before a given time
def printArivingAtBefore(fd,airport,arrTime):
    for aK in fd:
        for fK in fd[aK]:
            if fd[aK][fK][1][0]==airport and fd[aK][fK][1][1]<arrTime:
                depCity=fd[aK][fK][0][0].rjust(4)
                print(aK.rjust(15),str(fK).rjust(5),depCity, str(fd[aK][fK][0][0].rjust(4)))
'''printArivingAtBefore(flightsD,"MDW", 1200)'''


#print a formatted "flight board" for this dictionary for a given airline, all sorts
def printSortedAirlinesAndFlights(fD):
    airlineNameKeysList=list(fD.keys())
    airlineNameKeysList.sort()
    for airlineNameKey in airlineNameKeysList:
        print(airlineNameKey)
        flightNumKeysList=list(fD[airlineNameKey].keys())
        flightNumKeysList.sort()
        for flightNumKey in flightNumKeysList:
            print(str(flightNumKey).rjust(10))


#print airline flights from,to with a duration < given duration
def printflightsFromToDurationLessThan(fd,duration,depCity,arrCity):
    for airlineKey in fd:
        for flightNumKey in fd[airlineKey]:
            DCity=fd[airline][flightnumKey][0][0]
            depTime=fd[airline][flightnumKey][0][1]
            ACity=fd[airline][flightnumKey][1][0]
            arrTime=fd[airline][flightnumKey][1][1]
            if depTime<arrTime:
                actualDuration=arrTime-depTime
            else:
                actualDuration=2400+arrTime-depTime
            if ACity==arrCity and DCity==depCity and actualDuration<duration:
                print(airlineKey,flightNumKey, DCity, depTime, ACity, arrTime)

#printflightsFromToDurationLessThan(flightsD,600,"ALT",'LAX'):




def printDepartureArrivalBoards(fd,airline,airport):
    if airport!="": 
        print("DEPARTURES".center(30))
        lstOfFlights=[]
        for flightnumKey in fd[airline]:
            if fd[airline][flightnumKey][0][0]==airport:
                deCity=fd[airline][flightnumKey][0][0]
                depTime=fd[airline][flightnumKey][0][1]
                arrCity=fd[airline][flightnumKey][1][0]
                arrTime=fd[airline][flightnumKey][1][1]
                lstOfFlights.append([depTime,deCity,arrCity,arrTime])
        lstOfFlights.sort()
        for flight in lstOfFlights:
            print(flight[1].rjust(13),str(flight[0]).rjust(5),flight[3].rjust(4),str(flight[2]).rjust(5))
        #Now write the arrivels board
    else: #now all airports (no restriction via the paramater list)
        pass



printDepartureArrivalBoards(flightsD,'Delta',"MPW")






        
