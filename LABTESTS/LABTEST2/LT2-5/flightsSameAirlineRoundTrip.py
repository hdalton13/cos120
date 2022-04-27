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





#lst.append([str(aK),str(fK).rjust(5), str(fd[aK][fK][0][0]).rjust(4),str(arrTime).rjust(4),str(fd[aK][fK][1][0]).rjust(4),str(dTime).rjust(4)])

