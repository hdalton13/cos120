#Problem of the day

"""Problem of the Day - The rotational cipher will take each
character and shift it, starting with a shift of one, two for the
second character, three for the third, etc. until maxRotatenum is used,
then it will reset to one and repeat these shift rotations until all of
the characters in plainText have been encoded."""

def rotationalCypher(plainText,maxRotateNume):
    string=""
    q=1
    for i in range(len(plainText)):
        order= ord(plaintext)+q
        if q<=maxRotateNume:
            q+= 1
        string= string+ chr(order)
    return string
rotationalCypher(plainText,maxRotateNume)
    
def rotationalDecypher(cypherText,maxRotateNume):
