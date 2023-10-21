# Program to simulate the monty hall problem n times
import random

numTrials = 0 # the amount of trials to complete
# switch = True # if '1' the function will switch its selection; if '0' the function will keep its selections
def montyHall(numIter, switch):
    winCount = 0
    while numIter != 0:
        sampList = [1,-1,-2]
        random.shuffle(sampList) # shuffling the list
        selection = sampList[random.randint(0,2)] # the selected element
        # for loop removes one of the bad values
        for n in sampList:
            if (n != selection) and (n == -2 or n == -1):
                sampList.remove(n)
                break
        # this switches the selection to the other card after the elimination
        if switch == 1:
            if selection == 1:
                selection = -1
            else:
                selection = 1
        if selection > 0:
            winCount = winCount + 1
        numIter = numIter - 1
    return winCount

# This is a simplified approach to the monty hall problem. Essentially, if the initial selection is a win, 
# then the result will be a loss, and if the initial selection is a loss, it will always be a win
def montyHallSimplified(numIter, switch):
    winCount = 0
    while numIter != 0:
        sampList = [1,-1,-2]
        random.shuffle(sampList) # shuffling the list
        selection = sampList[random.randint(0,2)] # the selected element
        if switch == 1:
            if selection == 1:
                pass
            else:
                winCount = winCount + 1
        elif switch == 0:
            if selection == 1:
                winCount = winCount + 1
            else:
                pass
        numIter = numIter - 1
    return winCount

switch = int(input("After one of the incorrect choices are eliminated, do you want to computer to switch its selection?\n If yes, type '1' if no, type '0': "))
numTrials = int(input("How many trials do you wish to run? "))
print("There was a cumulative " + str(round(montyHallSimplified(numTrials,switch)/numTrials  * 100,2)) + "% success rate.")