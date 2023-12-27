import random

# Gets the lower and upper bounds from user
def GetRange():
    global lowest
    global highest
    lowest = int(input('Enter lowest number in range: '))
    highest = int(input('Enter highest number in range: '))

GetRange()
validRange = False

# input validation for range
while(validRange == False):
    if (lowest > highest):
        validRage = False
        print("invalid range: lowest number should be less than or equal to highest number")
        GetRange()
    elif (highest - lowest < 5):
        validRange = False
        print("invalid range: Please enter a range of five or more")
        GetRange()
    else:
        validRange = True
        randNum = random.randint(lowest, highest)

# Gets the first guess from the user
userGuess = int(input("Number generated. Make your guess: "))

# initializes the count that keeps track of the number of guesses it takes the user
numOfGuesses = 0

# While loop that runs until the uswer guesses the correct number
while(userGuess != randNum):

    # input validation to make sure the number guessed is in the given range
    if (userGuess > highest or userGuess < lowest):
        print("Out of range, please enter a number between", lowest , " and " , highest)

    # prints higher or lower depending on the guess
    elif (userGuess < randNum):
        print('My number is higher. Guess again')
    elif (userGuess > randNum):
        print('My number is lower. Guess again')

    # count increases for every guess
    numOfGuesses += 1
    # new input taken in
    userGuess = int(input())

# prints plural or singular guess depending on the number of guesses
if (numOfGuesses >= 1):
    print('You Got It! It took you' , numOfGuesses + 1 , 'guesses. Good job!')
else:
    print('You Got It! It took you' , numOfGuesses + 1 , 'guess. Good job!')
