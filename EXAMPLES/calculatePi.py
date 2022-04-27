from math import *

def archimedes(numOfsides):
    innerAngleB = 360.0/numOfsides  		#degrees in circle/number segments
    halfAngleA = innerAngleB/2.0    		#because we need a right triangle
    sideS = (sin(radians(halfAngleA)))*2       	#math.sin requires radians
    polygonCircumference = numOfsides * sideS 	#multiply # sides by length of each
    pi = polygonCircumference/2.0		#π = C/2r, but assumed a unit circle
    return pi

def leibniz(numTerms):
    piApprox=0
    numerator=4
    denominator=1
    multiplier=1
    for aTerm in range(numTerms):
        nextTerm=numerator/denominator * multiplier
        piApprox=piApprox+nextTerm
        multiplier=multiplier * -1
        denominator=denominator  +  2
    return piApprox

def wallis(numPairs):
    acc=1
    numerator=2
    for aPair in range(numPairs):
        leftTerm=numerator/(numerator-1)
        rightTerm=numerator/(numerator+1)
        acc=acc*leftTerm*rightTerm
        numerator=numerator+2
    piApprox=acc*2
    return piApprox

print("Pi=", pi)
print("Archimedies=",archimedes(800000000000000000000000))
print("Leibniz",leibniz(8000000))
print("Wallis=",wallis(8000000))
