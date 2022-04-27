import math
class Planet:
    def __init__(self, iname, iradius, imass, idistance,imoons): 
        self.__name = iname
        self.radius = iradius
        self.mass = imass
        self.distance = idistance
        self.numMoons= imoons
        self.moonLst=[]

    def getName(self):
        return self.__name
    
    def getnumMoons(self):
        return len(self.moonLst)
    
    def getCircumference(self):
        return 2 * math.pi * self.radius

    def setName(self,newName):
        self.__name=newName

    def addMoons(self,newMoonName):
        self.moonLst.append(newMoonName)
        
    def   __str__(self):
        return  self.name
        

p1=Planet("Z234",3000,2000,120000,6)
print(p1.name)
print(p1.getName())
print(p1.getnumMoons())
p2=Planet("QQQ777",5000,8000,10000,7)
print(p2.name)
print(p2.getName())
print(p2.getnumMoons())
p2.setName("Earth")
print(p2.getName())


class Sentence:
    def __init__(self,theSentence):
        self.sentence=theSentence

    def getSentance(self):
        return self.sentence

    def getWords(self):
        return self.sentence.split()

    def getLength(self):
        return len(self.sentence)

    def getNumWords(self):
        return len(self.getWords())
    
    def setUpper(self):
        self.sentence=self.sentence.upper()


x=Sentence("Hello world")
print(x.sentence)
print(x.getNumWords())




class Sentence2:
    def __init__(self,theSentence):
        self.sentenceWordList=theSentence.split()

    def getSentance(self):
        sent=""
        for word in self.sentenceWordList:
            sent= sent+word+""
        return sent[:-1]

    def getWords(self):
        return self.sentenceWordList

    def getLength(self):
        return len(self.getSentance())

    def getNumWords(self):
        return len(self.sentenceWordList)

y=Sentence("Hello world")
print(y.sentence)
print(y.getNumWords())


