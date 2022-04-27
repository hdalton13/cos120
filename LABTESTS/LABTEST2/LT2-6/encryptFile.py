##def reverse(s): 
##  str = "" 
##  for i in s: 
##    str = i + str
##  return str
##
##def encryptFile(inFile,outFile):
##    reading=open(inFile,"r")
##    out=open(outFile,"w")
##    index=1
##    for aline in reading:
##      if index%2==0:
##          changed= reverse(aline)
##          out.write("%s \n" %changed)
##          
##          print(index,"%s" %changed)
##          index+=1
##      else:
##          newS=""
##          line=aline.split()
##          for i in line:
##              newS+= reverse(i)+" "
##          print("%s" %newS[:-1])
##          out.write("%s \n" %newS[:-1])
##          index+=1
##    reading.close()
##    out.close()
##
##encryptFile("in.txt","out.txt")


def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def encryptFile(inFile,outFile):
    reading=open(inFile,"r")
    out=open(outFile,"w")
    index=1
    lst=[]
    for aline in reading:
      if index%2==0:
          changed= str(reverse(aline))
          lst.append(changed[1:])
          index+=1
      else:
          newS=""
          line=aline.split()
          for i in line:
              newS+= reverse(i)+" "
          lst.append(newS[:-1])
          index+=1
    print(lst)
    for line in lst:
      print(str(line))
      out.write("%s \n"%line)
    reading.close()
    out.close()

encryptFile("in.txt","out.txt")
