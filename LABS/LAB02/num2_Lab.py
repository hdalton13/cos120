#Heather Dalton
#Lab_2 (0-14)

def L_0():
   print("#0")
   for i in range(10,21): 
        print(i)
    

def L_1():
    print("")
    print("#1")
    for i in range(6):
       print(i)
    print("")

def L_2():
    print("#2")
    for i in range(1,6):
       print(i)
    print("")

def L_3():
    print("#3")
    for i in range(1,101):
        print(i)
    print("")

def L_4():
    print("#4")
    num=100
    for i in range(100,0,-1):
       print(i)
    print("")

def L_5():
    print("#5")
    for i in range(3,34,3):
       print(i)
    print("")

def L_6():
    print("#6")
    for i in range(33,2,-3):
       print(i)
    print("")
    
def L_7():
    print("#7")
    total=0
    for i in range(1,11):
       total= total+i
    print(total)
    print("")
    
def L_8():
    print("#8")
    mult=1
    for i in range(1,10):
       mult= mult*i
    print(mult)
    print("")

def L_9():
    print("#9")
    for name in ["Mary", "Joe", "Adam"]:
        for num in range(1,4):
            print(num, name)
    print("")
    
def L_10():
    print("#10")
    for name in ["Mary", "Joe", "Adam"]:
       for num in range(5,11):
            print(num, name)
    print("")
    
def L_11():
    print("#11")
    astric="*"
    for num in range(1,6):
        for i in range(num):
            print("*", end="")
        print("")
            
    print("")
    
def L_12():
    print("#12")
    for num in range(5,0,-1):
        for i in range(num):
            print("*", end="")
        print("")
    print("")
    
def L_13():
    print("#13")
    for name in range(1,4):
       for num in range(1,4):
            print(name, "X",num,"=",(num*name))
    print("")

def L_14():
    print("#14")
    start= int(input("Starting number"))
    end= int(input("Endinging number"))

    for name in range(start,end):
       for num in range(start,end):
            print(name, "X",num,"=",(num*name))
    print("")
    
def main1_8():
    L_0()
    L_1()
    L_2()
    L_3()
    L_4()
    L_5()
    L_6()
    L_7()
    L_8()
def main9_14():
    L_9()
    L_10()
    L_11()
    L_12()
    L_13()
    L_14()
    

    
main9_14()
