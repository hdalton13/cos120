from cImage import *
import sys
##sys.path.append("X:/COS 120 Introduction to Computational Problem Solving/Labs/LAB10/")
##from LAB10Solutions import *

def showImage(imageFileName):
    pict=FileImage(imageFileName)
    myWin = ImageWin("Image Processing",pict.getWidth(),pict.getHeight())
    pict.draw(myWin)
    p=Pixel(0,0,0)
    for i in range(100):
        x,y = myWin.getMouse()
        print(x,y)
        print(pict.getPixel(x,y))
        pict.setPixel(x,y,p)
    myWin.exitOnClick()
#showImage("stmarks.gif")
    
def createEmptyImage():
    myImWin = ImageWin("Empty Image", 300, 300) 
    emptyIm = EmptyImage(300, 300) 
    p=Pixel(100,100,150)
    p2=Pixel(100,37,200)
    for row in range(300):
        for col in range(300):
            if row > 200:
                emptyIm.setPixel(col,row,p2)
            else:
                emptyIm.setPixel(col,row,p)
    emptyIm.draw(myImWin)

def lineImage():
    myImWin = ImageWin("Line Image",300,300)
    lineImage = EmptyImage(300,300)
    whitePixel = Pixel(255, 255, 255)
    blackPixel = Pixel(0, 0, 0)
    for col in range(300):
        for row in range(300):
            lineImage.setPixel(col,row,blackPixel)
    for i in range(300):
        lineImage.setPixel(i, i, whitePixel)
        lineImage.draw(myImWin)
    lineImage.save("lineImage.gif")
    myImWin.exitOnClick()


def showGrayScale():
    myImWin = ImageWin("ShowGrayScale",340,340)
    lineImage = EmptyImage(340,340)
    for row in range(17):
        for col in range(17):
            for x in range(21):
                for y in range(21):
                    lineImage.setPixel(col*20+y,row*20+x,Pixel(row*col-1,row*col-1,row*col-1))
    lineImage.draw(myImWin)
    for i in range(10):
        pos = myImWin.getMouse()
        print(lineImage.getPixel(pos[0],pos[1]))
    myImWin.exitOnClick()


def negativePixel(oldPixel):
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel

def makeNegative(imageFile):
    oldimage = FileImage(imageFile)
    width = oldimage.getWidth()
    height = oldimage.getHeight()    
    myimagewindow = ImageWin("Image Processing", width*2, height)
    oldimage.draw(myimagewindow)
    newim = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = negativePixel(originalPixel)
            newim.setPixel(col,row,newPixel)
    newim.setPosition(width+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

def grayScalePixel(oldpixel):
     intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
     aveRGB = intensitySum//3
     newPixel = Pixel(aveRGB,aveRGB,aveRGB) 
     return newPixel

def makeGrayScale(imageFile):
    oldimage = FileImage(imageFile)
    myimagewindow = ImageWin("Image Processing", oldimage.getWidth()*2, oldimage.getHeight())
    oldimage.draw(myimagewindow)
    newim = EmptyImage(oldimage.getWidth(), oldimage.getHeight())
    for row in range(oldimage.getHeight()):
        for col in range(oldimage.getWidth()):
            originalPixel = oldimage.getPixel(col,row) 
            newPixel = grayScalePixel(originalPixel) 
            newim.setPixel(col,row,newPixel)
    newim.setPosition(oldimage.getWidth() + 1, 0) 
    newim.draw(myimagewindow) 
    myimagewindow.exitOnClick()

def pixelMapper(imageFile,rgbFunction):
    oldImage = FileImage(imageFile) 
    width = oldImage.getWidth() 
    height = oldImage.getHeight() 
    myimagewindow = ImageWin("Image Processing", width*2+1, height)     
    oldImage.draw(myimagewindow)
    newIm = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col,row) 
            newPixel = rgbFunction(originalPixel) 
            newIm.setPixel(col,row,newPixel)
    newIm.setPosition(width + 1, 0) 
    newIm.draw(myimagewindow) 
    myimagewindow.exitOnClick()

def mathManip(num1,num2,mathFunction):
    result=mathFunction(num1,num2)
    return result

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

import math
def hypotenuse(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

def modifyList(aList):
    aList[0]=99

def modifyInteger(anInt):
    anInt=anInt+1

def modifyString(aString):
    aString=aString.upper()
    #print(aString)


def halve(imageFile):
    oldImage = FileImage(imageFile) 
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
halve("stmarks.gif")

def double(imageFile):
    oldImage = FileImage(imageFile) 
    oldw = oldImage.getWidth()
    oldh = oldImage.getHeight()
    newim = EmptyImage(oldw*2,oldh*2)
    myimagewindow = ImageWin("Image Processing", oldw*2,oldh*2)     
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = oldImage.getPixel(col,row)
            newim.setPixel(2 * col, 2 * row,oldpixel)
            newim.setPixel(2 * col + 1, 2 * row,oldpixel)
            newim.setPixel(2 * col , 2 * row + 1,oldpixel)
            newim.setPixel(2 * col + 1, 2* row+1,oldpixel)
    newim.draw(myimagewindow) 
    myimagewindow.exitOnClick()

def double2(imageFile):
    oldImage = FileImage(imageFile) 
    oldw = oldImage.getWidth()
    oldh = oldImage.getHeight()
    newim = EmptyImage(oldw*2,oldh*2)
    myimagewindow = ImageWin("Image Processing", oldw * 2,oldh * 2)
    for col in range(0,newim.getWidth()):
        for row in range(0,newim.getHeight()):
            originalCol = col//2
            originalRow = row//2
            #print(originalCol,originalRow)
            oldpixel = oldImage.getPixel(originalCol,originalRow)
            newim.setPixel(col,row,oldpixel)
    newim.draw(myimagewindow) 
    myimagewindow.exitOnClick()

def scaleUpImage(imageFile,scale):
    oldImage = FileImage(imageFile) 
    oldw = oldImage.getWidth()
    oldh = oldImage.getHeight()
    newim = EmptyImage(oldw*scale,oldh*scale)
    myimagewindow = ImageWin("Scale-Up Processing", oldw*scale, oldh*scale)     
    for row in range(oldh): #Iterate through the old image row
        for col in range(oldw): #Iterate through the old image cols
            oldPixel = oldImage.getPixel(col,row)
            for rOffSet in range(scale): #Iterate to create pixel locations in new image
                for cOffSet in range(scale):                   
                    newim.setPixel(scale*col+cOffSet, scale*row+rOffSet, oldPixel)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()

def flip(imageFile):
    oldImage = FileImage(imageFile) 
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    newim = EmptyImage(width,height)
    myimagewindow = ImageWin("Image Processing", width, height)     
    for row in range(height):
        for col in range(width):
            oldpixel = oldImage.getPixel(col,row)
            newim.setPixel(width-1-col,height-1-row,oldpixel)
    newim.draw(myimagewindow) 
    myimagewindow.exitOnClick()
