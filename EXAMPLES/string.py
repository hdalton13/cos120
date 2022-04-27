#09/16/2019
name="Heather R Dalton"
print(name[0:name.find(" ")+1])
print(name[:8])
print(name[9:])
print(name[9:]+", "+name[:8])

s='s'
p='p'
print("mi"+2*s+'i'+2*s+'i'+2*p+'i')

for index in range(0,len(name)):
    print(name[:index])                 #don't need to hard code the Zero in


print('')
m=("mi"+2*s+'i'+2*s+'i'+2*p+'i')
print(m.count("s",4))
print(m.replace("iss","ox"))
print(m.find('m'))
print(m.find('z'))


print('')
print("python".center(20).upper())
print("python".upper().center(20))


#'A'=65
#'a'=95

print('')
print(ord('C')              #gives the ASCII value
print(chr(234567)           #gives the ASCII value
