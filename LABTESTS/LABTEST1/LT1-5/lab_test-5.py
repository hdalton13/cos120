#heather dalton
#09/26/19  @1:37

def stringProgression(string):
    new=""
    index=1
    for i in range(len(string)):
        if(i==index):
            new= new+ string[i]
            index=index*2
    return new

print(stringProgression("This is a test, this is only a test."))
print(stringProgression("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure."))
