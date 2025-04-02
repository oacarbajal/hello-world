# Lab 7-3 The Dice Game
# Omar Carbajal
# add libraries needed
import random

# the main function
def main():
    print()
# initialize variables
endProgram = "no"
playerTwo = 'NO NAME'
playerOne = 'NO NAME'

# call to inputNames
def inputNames():
    playerOne = input('Enter player 1 name: ')
    playerTwo = input('Enter player 2 name: ')
    return playerOne, playerTwo
# while loop to run program again
while endProgram == 'no':
# populate variables
    p1number = 0
    p2number = 0
    winnerName = 'NO NAME'

 # call to rollDice
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
 # call to displayInfo
    endProgram = input('Do you want to end program? (yes/no): ')
#this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne= input('Enter player 1 name: ')
    playerTwo= input('Enter player 2 name: ')
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number == p2number:
        winnerName = "TIE"
    elif p1number>p2number:
        winnerName=playerOne
    else:
        winnerName=playerTwo
    return winnerName
    return playerOne, playerTwo

#this function displays the winner

def displayinfo(winnerName):
    print('The winner is' , winnerName)

# calls main
main()