#09/30/19

"""Write a function that will accept exactly 1000
integers from the user, print the average of those
1000 numbers, and then print out how many of the
1000 integers are larger than the average."""

def countGTaverage():
    lst=[]
    accum=0
    for i in range(5):
        lst.append(int(input("please enter an integer =>")))
        accum=accum+lst[i]
    #print(lst)
  
    average=sum(lst)/len(lst)
    print(average)
    count=0
    for idx in range(len(lst)):
        if  lst[idx]>average:
            count+=1
    print("Number of items greater than", average,"is", count)

countGTaverage()
