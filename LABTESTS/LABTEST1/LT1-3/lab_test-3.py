#heather dalton
#09/26/2019 @12:40-paused@1:06

def idrawRightTrianglefromL(rows):
    for num in range(rows,0,-1):
        for i in range(num):
            print("*", end="")
        print("")
    print("")



def drawRightTriangleInverted(rows):
    space=""
    for i in range(rows,0,-1):
        print(space+"*"*i,end="")
        print("")
        space=" "+space
    print("")

drawRightTriangleInverted(6)
drawRightTriangleInverted(12)


