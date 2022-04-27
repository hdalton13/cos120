#Heather Dalton
#09/28/19
"""The following is results of running a function called guessingGame.
Write this function in a file called guessingGame.py.  When it is running correctly,
submit it to Moodle.  Your game will produce results similar to the following:"""

import random

def guessingGame(startCount, stopInclusive, numGuesses):
    answer= random.randrange(startCount,(stopInclusive+1))
    print("You are to guess a number between "+str(startCount)+" and "+str(stopInclusive)+ " inclusive, in "+str(numGuesses)+" guesses or less!")
    guess=0
    for i in range(numGuesses):
        guess= int(input("Enter your guess"))
        if (guess==answer):
            print("You quessed it!!!")
            return
        elif(guess<answer):
            print("LOW Guess")
        elif(guess>answer):
            print("HIGH Guess")
    if (guess != answer):
        print("You ran out of quesses")

guessingGame(0, 200, 10)
