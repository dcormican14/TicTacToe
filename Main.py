#Declaring the variables:
boardList = [["_","_","_"],["_","_","_"],["_","_","_"]]
cpuLogicList = [[2, 0, 2], [0, 4, 0], [2, 0, 2]]
inputStr = ""
outputBoolean = False
incrementVarX = 0
incrementVarY = 0
#Beginning the game
def askForPlayers():
    selectionStr = input("How many Players will be playing? (One/Two)")
    if(selectionStr.lower() == "one"):
        printTheBoard()
        playerPlaceTile()
    elif(selectionStr.lower() == "two"):
        printTheBoard()
        playerOnePlaceTile()
    else:
        print("\"" + selectionStr + "\"" + " is not an accepted input. Please try again.")
        print("---")
        askForPlayers()

#Allows the player to place their tile and calls the computer method
def playerPlaceTile():
    inputStr = input("Where would you like to move?")
    try:
        if ((inputStr[0].lower() == "a" or inputStr[0].lower() == "b" or inputStr[0].lower() == "c") and boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] == "_"):
            boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] = "O"
            if (checkAllValues("O", int(inputStr[1]) - 1, ord(inputStr[0].lower()) - 97)):
                printTheBoard()
                print("You won!")
                playAgain()
            else:
                if (checkForFull()):
                    printTheBoard()
                    print("The game is a tie!")
                    playAgain()
                else:
                    computerPlaceTile()

        else:
            print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
            playerPlaceTile()
    except:
        print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
        print("except")
        playerPlaceTile()

#allows the computer to place its tile and calls the player method
def computerPlaceTile():
    incrementVarX = 0
    incrementVarY = 0
    largestInt = 0
    largestIndexX = 0
    largestIndexY = 0
    for x in boardList:
        for y in x:
            if(checkAllValues("X", incrementVarX, incrementVarY)):
                cpuLogicList[incrementVarX][incrementVarY] +=99
            if(checkAllValues("O", incrementVarX, incrementVarY)):
                cpuLogicList[incrementVarX][incrementVarY] +=66
            if (boardList[incrementVarX][incrementVarY] != "_"):
                cpuLogicList[incrementVarX][incrementVarY] = -1
            incrementVarY +=1
        incrementVarY = 0
        incrementVarX +=1
    incrementVarX = 0

    for i in range(3):
        for j in range(3):
            if(int(cpuLogicList[i][j]) >= int(largestInt)):
                largestIndexX = i
                largestIndexY = j
                largestInt = cpuLogicList[i][j]
    boardList[largestIndexX][largestIndexY] = "X"
    printTheBoard()
    print("Computer placed their tile.")
    if(checkAllValues("X", largestIndexX, largestIndexY)):
        print("The computer won!")
        playAgain()
    else:
        if(checkForFull()):
            print("The game is a tie!")
            playAgain()
        else:
            playerPlaceTile()

#Allows for player one to place their tile and calls the player two method
def playerOnePlaceTile():
    inputStr = input("Where would player one like to move?(ex." + "\"" + "B3" + "\"" +")")
    try:
        if ((inputStr[0].lower() == "a" or inputStr[0].lower() == "b" or inputStr[0].lower() == "c") and boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] == "_"):
            boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] = "O"
            if(checkAllValues("O", int(inputStr[1]) - 1, ord(inputStr[0].lower()) - 97)):
                printTheBoard()
                print("Player one won!")
                playAgain()
            else:
                if(checkForFull()):
                    printTheBoard()
                    print("The game is a tie!")
                else:
                    printTheBoard()
                    playerTwoPlaceTile()

        else:
            print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
            playerOnePlaceTile()
    except:
        print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
        playerOnePlaceTile()

#Allows for player two to place their tile and calls the player one method
def playerTwoPlaceTile():
    inputStr = input("Where would player two like to move?")
    try:
        if ((inputStr[0].lower() == "a" or inputStr[0].lower() == "b" or inputStr[0].lower() == "c") and boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] == "_"):
            boardList[int(inputStr[1]) - 1][ord(inputStr[0].lower()) - 97] = "X"
            if (checkAllValues("X", int(inputStr[1]) - 1, ord(inputStr[0].lower()) - 97)):
                printTheBoard()
                print("Player two won!")
                playAgain()
            else:
                if (checkForFull()):
                    printTheBoard()
                    print("The game is a tie!")
                    playAgain()
                else:
                    printTheBoard()
                    playerOnePlaceTile()
        else:
            print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
            playerTwoPlaceTile()
    except:
        print("\"" + inputStr + "\"" + " is not an accepted input, please enter again.")
        playerTwoPlaceTile()

#Prints the board after the most recent move
def printTheBoard():
     print("   A    B    C")
     print("1  "+boardList[0][0]+" |  "+boardList[0][1]+"  | "+boardList[0][2]+" ")
     print("  ---|-----|---")
     print("2  "+boardList[1][0]+" |  "+boardList[1][1]+"  | "+boardList[1][2]+" ")
     print("  ---|-----|---")
     print("3  "+boardList[2][0]+" |  "+boardList[2][1]+"  | "+boardList[2][2]+" ")

def checkUpLeft(checkVar, row, col):
    try:
        if(checkVar == boardList[row-1][col-1]):
            return True
        else:
            return False
    except:
        return False
def checkUp(checkVar, row, col):
    try:
        if(checkVar == boardList[row-1][col]):
            return True
        else:
            return False
    except:
        return False
def checkUpRight(checkVar, row, col):
    try:
        if(checkVar == boardList[row-1][col+1]):
            return True
        else:
            return False
    except:
        return False
def checkLeft(checkVar, row, col):
    try:
        if(checkVar == boardList[row][col-1]):
            return True
        else:
            return False
    except:
        return False
def checkRight(checkVar, row, col):
    try:
        if(checkVar == boardList[row][col+1]):
            return True
        else:
            return False
    except:
        return False
def checkDownLeft(checkVar, row, col):
    try:
        if(checkVar == boardList[row+1][col-1]):
            return True
        else:
            return False
    except:
        return False
def checkDown(checkVar, row, col):
    try:
        if(checkVar == boardList[row+1][col]):
            return True
        else:
            return False
    except:
        return False
def checkDownRight(checkVar, row, col):
    try:
        if(checkVar == boardList[row+1][col+1]):
            return True
        else:
            return False
    except:
        return False
def checkMainLocation(checkVar, row, col):
    try:
        if(checkVar == boardList[row][col]):
            return True
        else:
            return False
    except:
        return False

#Calls all check methods from above and returns true if all 3 are in a row
def checkAllValues(checkVar, row, col):
    if(row == 1):
        if(checkUp(checkVar, row, col) and checkDown(checkVar, row, col)):
            return True
    if(col == 1):
        if(checkLeft(checkVar, row, col) and checkRight(checkVar, row, col)):
            return True
    if(col == 1 and row == 1):
        if(checkUpLeft(checkVar, row, col) and checkDownRight(checkVar, row, col)):
            return True
        elif(checkUpRight(checkVar, row, col) and checkDownLeft(checkVar, row, col)):
            return True
    if(row == 0):
        if(checkDown(checkVar, row, col) and checkDown(checkVar, row+1, col)):
            return True
    if(row == 2):
        if (checkUp(checkVar, row, col) and checkUp(checkVar, row-1, col)):
            return True
    if(col == 0):
        if (checkRight(checkVar, row, col) and checkRight(checkVar, row, col+1)):
            return True
    if(col == 2):
        if (checkLeft(checkVar, row, col) and checkLeft(checkVar, row, col-1)):
            return True
    if(row == 0 and col == 0):
        if(checkDownRight(checkVar, row, col) and checkDownRight(checkVar, row+1, col+1)):
            return True
    if(row == 2 and col == 0):
        if (checkDownLeft(checkVar, row, col) and checkDownLeft(checkVar, row + 1, col - 1)):
            return True
    if (row == 0 and col == 2):
        if (checkUpRight(checkVar, row, col) and checkUpRight(checkVar, row - 1, col + 1)):
            return True
    if (row == 2 and col == 2):
        if (checkUpLeft(checkVar, row, col) and checkUpLeft(checkVar, row - 1, col - 1)):
            return True
    return False

#Sees if all 9 spots are full
def checkForFull():
    for x in boardList:
        for y in x:
            if(y=="_"):
                return False
                break
    return True

#Asks the player if they would like to play again
def playAgain():
    yesNoStr = input("Would you like to play again?(yes/no)")
    try:
        if(yesNoStr.lower() == "y" or yesNoStr.lower() == "yes"):
            askForPlayers()
        elif(yesNoStr.lower() == "n" or yesNoStr.lower() == "no"):
            print("Thanks for playing!")
        else:
            print("\"" + yesNoStr + "\"" + " is not an accepted input. Please try again.")
            playAgain()
    except:
        print("\"" + yesNoStr + "\"" + " is not an accepted input. Please try again.")
        playAgain()


#Rules Block
print("Welcome to Tic-Tac-Toe!")

#Asks the player if they would like the rules.
def gameRules():
    yesNoStr = input("Would you like to see the rules? (yes/no)")
    try:
        if(yesNoStr.lower() == "y" or yesNoStr.lower() == "yes"):
            print("---")
            input("The player with the \"O\" tile goes first.")
            print("---")
            input("Players take turns placing their tiles in the squares.")
            print("---")
            input("To place a tile, type the column then the row you wish to place it in (ex. \"B3\")")
            print("---")
            input("The first player to connect 3 tiles in a row wins the game.")
            print("---")
            input("If all 9 tiles are filled and no players have connected 3 tiles in a row, the game is a tie.")
            print("---")
            input("Good luck!")
        elif(yesNoStr.lower() == "n" or yesNoStr.lower() == "no"):
            print("Good luck!")
        else:
            print("\"" + yesNoStr + "\"" + " is not an accepted input")
            gameRules()
    except:
        print("\"" + yesNoStr + "\"" + " is not an accepted input")
        gameRules()

#Start the game
gameRules()
askForPlayers()
