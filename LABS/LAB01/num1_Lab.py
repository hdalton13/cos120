#Lab Problem 01_01
print("Lab Problem 01_01")

#name= input("What is your first name?")
#last= input("What is your last name?")

#print("Hello", name)
#print("Hello", name + "!")
#print(name, "Hello")
#print(name, name, name, name)
#print(name, last)
#print(name+",", last)
#print("")

#Lab Problem 01_02
print("Lab Problem 01_02")

#earth_weight= input("What is your earth weight in pounds?")
#earth= int(earth_weight)
#print("Your Earth weight:", earth)
#moon= earth * 0.17
#print("Your Moon weight:", moon)
#mercury= earth * 0.38
#print("Your Mercury weight:", mercury)
#venus= earth * 0.91
#print("Your Venus weight:", venus)
#saturn= earth * 1.06
#print("Your Saturn weight:", saturn)
#jupiter= earth * 2.34
#print("Your Jupiter weight:", jupiter)
#print("")

#Lab Problem 01_03
print("Lab Problem 01_03")

#gamble= input("How much money do you have avalible to gambile in Bitcoin:")
#current_price= input("What is Bitcoin's current price in the USD:")
#total_bit= float(gamble)/float(current_price)
#print("You could be the sorry owner of",total_bit,"Bitcoins")
#print("")

#Lab Problem 01_04
print("Lab Problem 01_04")

#MPG= miles divided by gallons
#entry_1= 234/10
#entry_2= 360/15
#entry_3= 200/10
#average= (entry_1+entry_2+entry_3)/3
#print("For entry 1 your MPG is", entry_1)
#print("For entry 2 your MPG is", entry_2)
#print("For entry 3 your MPG is", entry_3)
#print("Your average MPG for the three logbook entries is", average)

#Lab Problem 01_05
#
#print("Lab Problem 01_05")
#elapsed= float(input("Enter the total seconds you wish to convert to days, hours, minutes and seconds:"))

#day= elapsed//(60*60*24)
#elapsed= elapsed%(60*60*24)
#print("Day:", day)

#hour=elapsed//(60*60)
#elapsed=elapsed%(60*60)
#print("Hours:", hour)

#minutes= elapsed//(60)
#elapsed=elapsed%(60)
#print("Minutes:", minutes)

#seconds= elapsed
#print("Seconds:", seconds )

print("Runestone")

#Question 2.1
print("Question 2.1")

print(5 ** 2)
print(9 * 5)
print(15 / 12)
print(12 / 15)
print(15 // 12)
print(12 // 15)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
print("")

#Question 2.2
print("Question 2.2")
print("2 + (3 - 1) * 10 / 5 * (2 + 3)")
print("2 + (2) * 10 / 5 * (5)")
print("2 + 20 / 5 * (5)")
print("2 + 4 * (5)")
print("2 + 20")
print(2 + (3 - 1) * 10 / 5 * (2 + 3))
print("")

#Question 2.3
print("Question 2.3")
set_alarm= input("How long until your alarm should go off? (in hours)")
current_time= input("What time is it now in hours?")

time= (int(set_alarm) + int(current_time))

time= time%24
    
print(time)
print("")

#Question 2.4
print("Question 2.4")
day= input("What is the starting day number")
length =input("What is the length of your trip")
num_day= int(day)
num_length= int(length)

time= num_day + num_length
date= 6%time

print("you will come back on day #", date)
print("")

#Question 2.5
print("Question 2.5")
a= 'All'
w="work"
a2='and'
n= "no"
p='play'
m="makes"
j= 'Jack'
a3= "a"
d= 'dull'
b="doy."
print(a, w, a2, n, p, m, j, a3, d, b)
print("")

#Question 2.6
print("Question 2.6")
print(6*(1-2))
print("")

#Question 2.7
print("Question 2.7")
P=10000
n=12
r=0.08
num_years= input("How many years")
t=int(num_years)

A=P*((1+(r/n))**(n*t))
print(A, "after", t,"years")
print("")

#Question 2.8
print("Question 2.8")
r=int(input("What is the radius of the circle"))

A= (3.14*(r**2))
print("The area of the circle equals", A)






