from cImage import*

def sepiaPixel(p):
    newred = (p.getRed()*0.393 + p.getGreen()*0.769 + p.getBlue()* 0.189)/3
    newgreen = (p.getRed()*0.349 + p.getGreen()*0.686 + p.getBlue()* 0.168)/3
    newblue = (p.getRed()*0.272 + p.getGreen()*0.534 + p.getBlue()* 0.131)/3
    newPixel = Pixel(int(newred), int(newgreen), int(newblue))
    return newPixel

def blackAndWhite(p):
    threshold=128
    #threshold=input("whats your theshold?")
    average=(p.getRed()+p.getGreen()+p.getBlue())//3
    if average>threshold:
        r=255
        b=255
        g=255
    else:
        r=0
        b=0
        g=0
    return Pixel(r,g,b)

def grayPixel(p):
    nc=(p.getRed()+p.getGreen()+p.getBlue())//3
    return Pixel(nc,nc,nc)

def negativePixel(p):
    r=255-p.getRed()
    g=255-p.getGreen()
    b=255-p.getBlue()
    return Pixel(r,g,b)

def RGBAdjust(p,radj,gadj,badj):
    newred = int((radj * p.getRed())+ p.getRed())
    newgreen = int((gadj*p.getGreen())+ p.getGreen())
    newblue = int((badj*p.getBlue())+ p.getBlue())
    if newred>255:
        newred=255
    if newgreen>255:
        newgreen=255
    if newblue>255:
        newblue=255
    newPixel = Pixel(int(newred), int(newgreen), int(newblue))
    return newPixel

def halfSize(imageFile):
    oldImage = imageFile 
    oldw = oldImage.getWidth()
    oldh = oldImage.getHeight()
    newim = EmptyImage(oldw//2,oldh//2)
    myimagewindow = ImageWin("Image Processing", oldw+oldw//2,oldh)
    oldImage.draw(myimagewindow)
    for row in range(oldh//2):
        for col in range(oldw//2):
            p1=oldImage.getPixel(2 * col, 2 * row)
            p2=oldImage.getPixel(2 * col + 1, 2 * row)
            p3=oldImage.getPixel(2 * col , 2 * row + 1)
            p4=oldImage.getPixel(2 * col + 1, 2* row+1)
            r=(p1.getRed()+p2.getRed()+p3.getRed()+p4.getRed())//4
            g=(p1.getGreen()+p2.getGreen()+p3.getGreen()+p4.getGreen())//4
            b=(p1.getBlue()+p2.getBlue()+p3.getBlue()+p4.getBlue())//4
            newPixel=Pixel(r,g,b)
            newim.setPixel(col,row,newPixel)
    newim.setPosition(oldw+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()


def pixelMapper(rgbFunction,oldImage,title):
    width = oldImage.getWidth() 
    height = oldImage.getHeight() 
    myImageWindow = ImageWin(title, width*2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width,height)
    if rgbFunction == RGBAdjust:
        pRed=float(input("What percent would you like to increase Red?"))
        pBlue=float(input("What percent would you like to increase Blue?"))
        pGreen=float(input("What percent would you like to increase Green?"))
        for row in range(height):
            for col in range(width):
                originalPixel = oldImage.getPixel(col,row) 
                newPixel = rgbFunction(originalPixel,pRed,pGreen,pBlue)
                newIm.setPixel(col,row,newPixel)
    else:
        for row in range(height):
            for col in range(width):
                originalPixel = oldImage.getPixel(col,row) 
                newPixel = rgbFunction(originalPixel)
                newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1, 0) 
    newIm.draw(myImageWindow)
    return newIm


def imageProc(fname):
    if fname!="":
        myImage=FileImage(fname)
    else:
        myImage=""
    answer=0
    while answer != 9:
        if myImage !="":
            print("1) Load an image\n2) Adjust RGB values\n3) Produce a gray-scale image of the current image\n4) Produce a black and white of the current image\n5) Produce a sepia-toned image of the current image\n6) Produce a negative of the current image\n7) Reduce image size by 1/2 (1/4 the original pixels)\n8) Save the image\n9) Exit")
            answer=int(input("Select a menu choice => "))
            while answer not in [1,2,3,4,5,6,7,8,9]:
                print("1) Load an image\n2) Adjust RGB values\n3) Produce a gray-scale image of the current image\n4) Produce a black and white of the current image\n5) Produce a sepia-toned image of the current image\n6) Produce a negative of the current image\n7) Reduce image size by 1/2 (1/4 the original pixels)\n8) Save the image\n9) Exit")
                answer=int(input("Select a menu choice => "))
        else: #the default image is not present
            print("1) Load an image\n9) Exit")
            answer=int(input("Select a menu choice => "))
            while answer not in [1,9]:
                print("1) Load an image\n9) Exit")
                answer=int(input("Select a menu choice => "))
            
        if answer==1:
            imageFileName=str(input("type your image ('name.gif')==>"))
            myImage=FileImage(imageFileName)
            myWin = ImageWin("Image Processing",myImage.getWidth(),myImage.getHeight())
            myImage.draw(myWin)
            myWin.exitOnClick()

            
        elif answer==2:
            oldImage=FileImage(fname)
            newIm=pixelMapper(RGBAdjust,oldImage,"RGBAdjust")
            
            
        elif answer==3:
            newIm=pixelMapper(grayPixel,myImage,"Grayscale Image")

        elif answer==4:
            newIm=pixelMapper(blackAndWhite,myImage,"blackAndWhite Image")

        
        elif answer==5:
            newIm=pixelMapper(sepiaPixel,myImage,"sepiaPixel Image")

        elif answer==6:
            newIm=pixelMapper(negativePixel,myImage,"Negative Image")

        elif answer==7:
            newIm= halfSize(myImage)
            
        elif answer==8:
            question= str(input("what do you want to NAME your file?"))
            newIm.save(question)

      
imageProc("stmarks.gif")
