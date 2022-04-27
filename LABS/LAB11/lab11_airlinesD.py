#11/12/19

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
                   1102:[["BNA",1100],["HOU",1450]]}}


#L11-1 Write a function def printAirlines(airD): that will print out
#the names of all of the airlines in the dictionary (5 points)

def printAirlines(airD):    
    for key in airD:
        print(key)
printAirlines(flightsD)
print("")


#L11-2 Write a function def printAirlinesWithFlight(airD,withFlight): that will
#print out the names of all of the airlines in the dictionary with a
#flight 1102 (5 points)

def printAirlinesWithFlight(airD,withFlight):
    for key in airD:
        for i in airD[key]:
            #print(i)
            if i==withFlight:
                print(key)
printAirlinesWithFlight(flightsD,1102)
print("")

#L11-3 Write a function def printAirlineFlightNums(airD): that will
#print out the names of all of the airlines along with the flight numbers
#for all flights for that airline (10 points)

def printAirlineFlightNums(fd):
    aKeys=list(fd.keys())
    aKeys.sort()
    for airlineNameKey in aKeys:
        print(airlineNameKey)
        flKeys=list(fd[airlineNameKey].keys())
        flKeys.sort()
        for flightKey in flKeys:
            print(str(flightKey).rjust(10))
printAirlineFlightNums(flightsD)

#L11-4 Write a function def printAirlineFlightsDepartFrom(airD,fromCity):
#that will print all Airlines and the flights from that airline that depart
#from a specified city (10 points)

def printAirlineFlightsDepartFrom(airD,fromCity):
    for key in airD:
        for flightnum in airD[key]:
            if (airD[key][flightnum][0][0])==fromCity:
                print(key, flightnum)
        
    
printAirlineFlightsDepartFrom(flightsD,"ATL")
print("")

#L11-5 Write a function def printAirlineFlightNumsSorted(airD): that will
#print out the names of all of the airlines along with the flight numbers
#for all flights for that airline, but with the flights in sorted order per
#airline (10 points)

def printAirlineFlightNumsSorted(fD):
    airlineNameKeysList=list(fD.keys())
    airlineNameKeysList.sort()
    for airlineNameKey in airlineNameKeysList:
        print(airlineNameKey)
        flightNumKeysList=list(fD[airlineNameKey].keys())
        flightNumKeysList.sort()
        for flightNumKey in flightNumKeysList:
            print(str(flightNumKey).rjust(10))
printAirlineFlightNumsSorted(flightsD)
print("")

#L11-6 Write a function def printAirlinesFlightInfo(airD): that will
#print out the names of all of the airlines along with the flight numbers,
#departure city and time, and arrival city and time for all flights for
#that airline.  Be sure the time is formatted in civilian time (am or pm)
#(10 points)

def printAirlinesFlightInfo(fd):
    for aK in fd:
        print(aK.rjust(15))
        time="am"
        timed="am"

        for fK in fd[aK]:
            arrTime=fd[aK][fK][0][1]
            if arrTime>1200:
                arrTime=arrTime-1200
                time="pm"

            dTime=fd[aK][fK][1][1]
            if dTime>1200:
                dTime=dTime-1200
                timed="pm"

            print(str(fK).rjust(5), str(fd[aK][fK][0][0]).rjust(4),str(arrTime).rjust(4)+time,str(fd[aK][fK][1][0]).rjust(4),str(dTime).rjust(4)+timed)

printAirlinesFlightInfo(flightsD)

#L11-7 Write a function def printSelectedFlight(airD,airline,flightNum):
#that will print out the departure city and time, and arrival city and time
#for the specified flight for the specified airline.  Be sure the time is
#formatted in civilian time(am or pm) (10 points)

def printSelectedFlight(fd,airline,flightNum):
    for aK in fd:
        print(aK)
        time="am"
        timed="am"

        for fK in fd[aK]:
            if fK==flightNum:
                arrTime=fd[aK][fK][0][1]
                if arrTime>1200:
                    arrTime=arrTime-1200
                    time="pm"

                dTime=fd[aK][fK][1][1]
                if dTime>1200:
                    dTime=dTime-1200
                    timed="pm"

                print(str(fK).rjust(5), str(fd[aK][fK][0][0]).rjust(4),str(arrTime).rjust(4)+time,str(fd[aK][fK][1][0]).rjust(4),str(dTime).rjust(4)+timed)

            

printSelectedFlight(flightsD,'Delta',1102)
print("")

#L11-8 Write a function def findFlight(airD,fromCity,toCity): that will
#print out all Airlines and flight numbers and times that match the specified
#fromCity/toCity parameters.  Within Airlines, sort the flights by departure
#time (10 points)
def findFlight(fd,fromCity,toCity):
    for aK in fd:
        for fK in fd[aK]:
            if (fd[aK][fK][0][0])==fromCity and (fd[aK][fK][1][0])==toCity:
                arrTime=fd[aK][fK][0][1]
                if arrTime>1200:
                    arrTime=arrTime-1200
                    time="pm"

                dTime=fd[aK][fK][1][1]
                if dTime>1200:
                    dTime=dTime-1200
                    timed="pm"
                print(str(aK),str(fK).rjust(5), str(fd[aK][fK][0][0]).rjust(4),str(arrTime).rjust(4)+time,str(fd[aK][fK][1][0]).rjust(4),str(dTime).rjust(4)+timed)


findFlight(flightsD,"HOU","ATL")









