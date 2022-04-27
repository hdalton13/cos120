flightsD={"Delta":{1102:[["IND",1850],["MDW",1955]],
                   1096:[["PHX",900],["MDW",1255]],
                   1445:[["ATL",1135],["LAX",1810]],
                   1776:[["PHL",1350],["RAP",1610]],
                   1226:[["PHX",950],["MDW",1345]],
                   1885:[["ATL",1305],["LAX",2000]],
                   1009:[["MDW",1850],["IND",1955]],
                   9001:[["MDW",2145],["IND",2255]],
                   9005:[["MDW",830],["IND",930]]},
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

#fD["American"][4311][1][0]

#prints out the names of the airlines
def namesOfAirlines(fD):
    for airlineNameKey in fD:
        print(airlineNameKey)


#returns a list of the names of the airlines
def namesOfAirlinesList(fD):
    lstOfNames=[]
    for airlineNameKey in fD:
        lstOfNames.append(airlineNameKey)
    return lstOfNames

def namesOfAirlinesList(fD):
    return list(fD.keys())

def namesOfAirlinesList(fD):
    x = list(fD.keys())
    x.sort()
    return x

#print airlines and their flights
def printAirlinesAndFlights(fD):
    for airlineNameKey in fD:
        print(airlineNameKey)
        for flightNumKey in fD[airlineNameKey]:
            print(str(flightNumKey).rjust(10))

#print sorted airlines and their flights 
def printSortedAirlinesAndFlights(fD):
    airlineNameKeysList=list(fD.keys())
    airlineNameKeysList.sort()
    for airlineNameKey in airlineNameKeysList:
        print(airlineNameKey)
        flightNumKeysList=list(fD[airlineNameKey].keys())
        flightNumKeysList.sort()
        for flightNumKey in flightNumKeysList:
            print(str(flightNumKey).rjust(10))

#printSortedAirlinesAndFlights(flightsD)


#print airline flights arriving at a user specified airport
def printFlightsArrivingAt(fD,destAirport):
    for airlineKey in fD:
        for flightNumKey in fD[airlineKey]:
            if fD[airlineKey][flightNumKey][1][0]==destAirport:
                airLine=airlineKey.rjust(15)
                flightNum=str(flightNumKey).rjust(5)
                depCity=fD[airlineKey][flightNumKey][0][0].rjust(4)
                depTime=str(fD[airlineKey][flightNumKey][0][1]).rjust(4)
                arrCity=fD[airlineKey][flightNumKey][1][0].rjust(4)
                arrTime=str(fD[airlineKey][flightNumKey][1][1]).rjust(4)
                print(airLine,flightNum,depCity,depTime,arrCity,arrTime)
        
#printFlightsArrivingAt(flightsD,"MDW")  

            
#print airline flights arriving at a given airport before a given time
def printFlightsArrivingAtBefore(fD,destAirport,arrivalTime):
    for airlineKey in fD:
        for flightNumKey in fD[airlineKey]:
            if fD[airlineKey][flightNumKey][1][0]==destAirport and fD[airlineKey][flightNumKey][1][1] < arrivalTime:
                airLine=airlineKey.rjust(15)
                flightNum=str(flightNumKey).rjust(5)
                depCity=fD[airlineKey][flightNumKey][0][0].rjust(4)
                depTime=str(fD[airlineKey][flightNumKey][0][1]).rjust(4)
                arrCity=fD[airlineKey][flightNumKey][1][0].rjust(4)
                arrTime=str(fD[airlineKey][flightNumKey][1][1]).rjust(4)
                print(airLine,flightNum,depCity,depTime,arrCity,arrTime)

#print("\n"*4)
#printFlightsArrivingAtBefore(flightsD,"MDW",1200)



#print airline flights from,to with a duration < given duration
def printFlightsFromToDurationLessThan(fD,departureCity,arrivalCity,maxDuration):
    for airlineKey in fD:
        for flightNumKey in fD[airlineKey]:
            if fD[airlineKey][flightNumKey][0][0]==departureCity and fD[airlineKey][flightNumKey][1][0]== arrivalCity:
                if fD[airlineKey][flightNumKey][1][1] > fD[airlineKey][flightNumKey][0][1]:
                    duration=fD[airlineKey][flightNumKey][1][1]-fD[airlineKey][flightNumKey][0][1]
                else:
                    duration=fD[airlineKey][flightNumKey][1][1]+2400-fD[airlineKey][flightNumKey][0][1]
                if duration < maxDuration:
                    pass
                    
"""print a formatted "flight board" for this dictionary for a given airline sorted by time,
for departures and arrivals, and specified airport only if airport argument is not null"""
def printDeparturesArrivalsForAirlineForAirport(fD,airline,airport):
    if airport !="":
        print((airline+" DEPARTURES "+airport).center(40))
        flightsList=[]
        for flightNumKey in fD[airline]:
            if fD[airline][flightNumKey][0][0]==airport:
                flightsList.append([fD[airline][flightNumKey][0][1],fD[airline][flightNumKey][0][0],fD[airline][flightNumKey][1][1],fD[airline][flightNumKey][1][0],flightNumKey])
        flightsList.sort()
        for flight in flightsList:
            print(str(flight[4]).rjust(11),flight[1].rjust(4),str(flight[0]).rjust(5),flight[3].rjust(4),str(flight[2]).rjust(5))

        print((airline+" ARRIVALS "+airport).center(35))
        flightsList=[]
        for flightNumKey in fD[airline]:
            if fD[airline][flightNumKey][1][0]==airport:
                flightsList.append([fD[airline][flightNumKey][0][1],fD[airline][flightNumKey][0][0],fD[airline][flightNumKey][1][1],fD[airline][flightNumKey][1][0],flightNumKey])
        flightsList.sort()
        for flight in flightsList:
            print(str(flight[4]).rjust(11),flight[1].rjust(4),str(flight[0]).rjust(5),flight[3].rjust(4),str(flight[2]).rjust(5))

    else: #No airport specified, so print all city departures and arrivals
        pass
        
printDeparturesArrivalsForAirlineForAirport(flightsD,"Delta","MDW")
    
