import math

minBoardSize = 1
maxBoardSize = 10
playerOneMarker = 'X'
playerOneName = 'Player One'
playerTwoMarker = 'O'
playerTwoName = 'Player Two'
debug = False

size = 0
boardValues = [' ']
corners = []
topEdges = []
bottomEdges = []
leftEdges = []
rightEdges = []
centers = []


# Sets up the boardValues list and all six lists for where spaces are located.
def setBoard(board_size):
    global boardValues

    # Main Board
    for i in range(int(math.pow(board_size, 2) - 1)):
        boardValues.append(' ')

    # Top Edges
    for i in range(1, size - 1):
        topEdges.append(i)

    # Bottom Edges
    for i in range(1, size - 1):
        bottomEdges.append(i + (size * (size - 1)))

    # Left Edges
    for i in range(size, int(math.pow(size, 2) - size), size):
        leftEdges.append(i)

    # Right Edges
    for i in range(2 * size - 1, int(math.pow(size, 2) - size), size):
        rightEdges.append(i)

    # Centers
    for i in range(size + 1, int(math.pow(size, 2) - size - 1)):
        if i % size == 0 or (i + 1) % size == 0:
            continue
        centers.append(i)

    # corners[0] = Upper Left
    # corners[1] = Upper Right
    # corners[2] = Lower Left
    # corners[3] = Lower Right
    corners.append(0)
    corners.append(size - 1)
    corners.append(int(math.pow(size, 2) - size))
    corners.append(int(math.pow(size, 2) - 1))

    if size == 2:
        print("Wow, that is a complicated board.")
    elif size == 1:
        print("If you need a computer to help you play this game, you don't need to have a computer.")


def setPlayerOne(name):
    global playerOneName
    playerOneName = name


def setPlayerTwo(name):
    global playerTwoName
    playerTwoName = name


# Gets the size of the board from the user.
def getBoardSize():
    global size
    while True:
        while True:
            try:
                print("Enter a board size: ", end="")
                temp = int(input())
                break
            except ValueError:
                print("I know what you did, don't do it again.")
        if temp < minBoardSize or temp > maxBoardSize:
            print("Please enter a different board size.")
        else:
            size = temp
            setBoard(size)
            break


# Prints the board bare, without row and column labels.
def printBoardWithoutLabels():
    for j in range(size):
        for i in range(size):
            print(" " + boardValues[j * size + i] + " ", end="")
            if i < size - 1:
                print("|", end="")
        print()
        for i in range(size):
            if j == size - 1:
                break
            print("----", end="")
        print()


# Prints the board with row and column labels.
def printBoardWithLabels():
    temp = "   "
    for i in range(size):
        temp += str(i) + "   "
    print(temp)
    for j in range(size):
        print(str(j) + " ", end='')
        for i in range(size):
            print(" " + boardValues[j * size + i] + " ", end="")
            if i < size - 1:
                print("|", end="")
        print()
        print('  ', end='')
        for i in range(size):
            if j == size - 1:
                break
            print("----", end="")
        print()


# Converts the board to a string.
def boardToString():
    temp = ""
    for i in range(int(math.pow(size, 2))):
        temp += boardValues[i]
        if i != int(math.pow(size, 2) - 1):
            temp += ','
    return temp


def checkUpperLeft(start):
    startChar = boardValues[start]
    checkChar = boardValues[start - size - 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkUpper(start):
    startChar = boardValues[start]
    checkChar = boardValues[start - size]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkUpperRight(start):
    startChar = boardValues[start]
    checkChar = boardValues[start - size + 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkLeft(start):
    startChar = boardValues[start]
    checkChar = boardValues[start - 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkRight(start):
    startChar = boardValues[start]
    checkChar = boardValues[start + 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkDownLeft(start):
    startChar = boardValues[start]
    checkChar = boardValues[start + size - 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkDown(start):
    startChar = boardValues[start]
    checkChar = boardValues[start + size]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


def checkDownRight(start):
    startChar = boardValues[start]
    checkChar = boardValues[start + size + 1]
    if startChar == ' ':
        return False
    if startChar == checkChar:
        return True
    return False


# Checks for a winner by going the whole width of the board
def checkAllRows():
    allLeftEdges = [0]
    allLeftEdges.extend(leftEdges)
    allLeftEdges.append(corners[2])

    for i in range(len(allLeftEdges)):
        checkChar = boardValues[allLeftEdges[i]]
        if checkChar == ' ':
            continue
        tempCheck = True
        for j in range(size):
            tempCheck = tempCheck and (checkChar == boardValues[allLeftEdges[i] + j])
        if tempCheck:
            if debug:
                print("Row match found")
            return True
    return False


# Checks for a winner by going the whole height of the board
def checkAllColumns():
    allTopEdges = [0]
    allTopEdges.extend(topEdges)
    allTopEdges.append(corners[1])

    for i in range(len(allTopEdges)):
        checkChar = boardValues[allTopEdges[i]]
        if checkChar == ' ':
            continue
        tempCheck = True
        for j in range(size):
            tempCheck = tempCheck and (checkChar == boardValues[allTopEdges[i] + (j * size)])
        if tempCheck:
            if debug:
                print("Column match found")
            return True
    return False


# Checks both diagonals for a winner
def checkDiagonals():
    mainDiag = boardValues[0]
    tempCheck = False
    for i in range(size - 1):
        if i == 0:
            tempCheck = True
        if mainDiag == ' ':
            tempCheck = False
            break
        tempCheck = tempCheck and (mainDiag == boardValues[size * i + i + size + 1])
    if tempCheck:
        if debug:
            print("Main diagonal match found")
        return True

    tempCheck = True
    secondDiag = boardValues[corners[2]]
    for i in range(size):
        if secondDiag == ' ':
            tempCheck = False
            break
        tempCheck = tempCheck and (secondDiag == boardValues[corners[2] - (size * i) + i])

    if debug:
        if tempCheck:
            print("Second diagonal match found")

    return tempCheck


# Checks for a winner by looking for a box of four.
def checkBox():
    upperLeftSpot = checkRight(corners[0]) and checkDown(corners[0]) and checkDownRight(corners[0])
    upperRightSpot = checkLeft(corners[1]) and checkDown(corners[1]) and checkDownLeft(corners[1])
    lowerLeftSpot = checkUpper(corners[2]) and checkRight(corners[2]) and checkUpperRight(corners[2])
    lowerRightSpot = checkUpper(corners[3]) and checkLeft(corners[3]) and checkUpperLeft(corners[3])

    if upperLeftSpot or upperRightSpot or lowerLeftSpot or lowerRightSpot:
        if debug:
            print("Corner match found")
        return True

    for i in range(len(topEdges)):
        topChecks = [checkLeft(topEdges[i]),
                     checkDownLeft(topEdges[i]),
                     checkDown(topEdges[i]),
                     checkDownRight(topEdges[i]),
                     checkRight(topEdges[i])]
        if (topChecks[0] and topChecks[1] and topChecks[2]) \
                or (topChecks[2] and topChecks[3] and topChecks[4]):
            if debug:
                print("Top edge match found")
            return True

    for i in range(len(bottomEdges)):
        bottomCheck = [checkLeft(bottomEdges[i]),
                       checkUpperLeft(bottomEdges[i]),
                       checkUpper(bottomEdges[i]),
                       checkUpperRight(bottomEdges[i]),
                       checkRight(bottomEdges[i])]
        if (bottomCheck[0] and bottomCheck[1] and bottomCheck[2]) \
                or (bottomCheck[2] and bottomCheck[3] and bottomCheck[4]):
            if debug:
                print("Bottom Edge match found")
            return True

    for i in range(len(leftEdges)):
        leftCheck = [checkUpper(leftEdges[i]),
                     checkUpperRight(leftEdges[i]),
                     checkRight(leftEdges[i]),
                     checkDownRight(leftEdges[i]),
                     checkDown(leftEdges[i])]
        if (leftCheck[0] and leftCheck[1] and leftCheck[2]) \
                or (leftCheck[2] and leftCheck[3] and leftCheck[4]):
            if debug:
                print("Left edge match found")
            return True

    for i in range(len(rightEdges)):
        rightCheck = [checkUpper(rightEdges[i]),
                      checkUpperLeft(rightEdges[i]),
                      checkLeft(rightEdges[i]),
                      checkDownLeft(rightEdges[i]),
                      checkDown(rightEdges[i])]
        if (rightCheck[0] and rightCheck[1] and rightCheck[2]) \
                or (rightCheck[2] and rightCheck[3] and rightCheck[4]):
            if debug:
                print("Right edge match found")
            return True

    for i in range(len(centers)):
        centerCheck = [checkUpper(centers[i]),
                       checkUpperRight(centers[i]),
                       checkRight(centers[i]),
                       checkDownRight(centers[i]),
                       checkDown(centers[i]),
                       checkDownLeft(centers[i]),
                       checkLeft(centers[i]),
                       checkUpperLeft(centers[i])]
        if (centerCheck[0] and centerCheck[1] and centerCheck[2]) \
                or (centerCheck[2] and centerCheck[3] and centerCheck[4]) \
                or (centerCheck[4] and centerCheck[5] and centerCheck[6]) \
                or (centerCheck[6] and centerCheck[7] and centerCheck[0]):
            if debug:
                print("Center match found")
                print("Current search location: " + str(i))
            return True


# Helper function to check all winning combinations.
def isBoardSolved():
    return checkAllRows() or checkAllColumns() or checkDiagonals() or checkBox()


def isBoardFull():
    for i in range(len(boardValues)):
        if boardValues[i] == ' ':
            return False
    return True


def isSpacePlayable(spot):
    if boardValues[spot] != ' ':
        return False
    return True


def updateBoard(newBoard):
    global boardValues
    boardValues = newBoard.split(',')
    # print(boardValues)
    singleSideLogic()


# Asks the player where they would like to move. If the spot is occupied, it makes them choose a different space.
# It will return the grid space they wanted to play in.
def getMove(player):
    while True:
        while True:
            try:
                print(player + ", enter your move: ", end="")
                selection = input()
                temp = selection.split()
                column = int(temp[0])
                row = int(temp[1])
                if row >= size or row < 0 or column >= size or column < 0:
                    row = size + 1
                    column = size + 1
                attempted = column * size + row
                break
            except (ValueError, IndexError):
                print("That is not how you select a spot to play")
        try:
            if isSpacePlayable(attempted):
                return attempted
        except IndexError:
            print("\nThat isn't even on the board, pick something else.\n")
            printBoardWithLabels()
        else:
            print("Please select a different space, that location is occupied. ")
            printBoardWithLabels()


# Logic used when running the game locally
def controlLogic():
    activePlayer = 1
    winner = False

    while True:
        if activePlayer % 2 == 0:
            boardValues[getMove(playerTwoName)] = playerTwoMarker
        else:
            boardValues[getMove(playerOneName)] = playerOneMarker
        activePlayer += 1
        printBoardWithLabels()
        if isBoardSolved():
            winner = True
            break
        if isBoardFull():
            break

    print("\n" * 100)
    if winner:
        activePlayer -= 1
        if activePlayer % 2 == 0:
            print(playerTwoName + " wins", end='')
        else:
            print(playerOneName + " wins", end='')
        print(" after " + str(math.ceil(activePlayer / 2)) + " moves.")
        print("A total of " + str(activePlayer) + " moves were made.")
    else:
        print("Good game, nobody won this time.")

    printBoardWithLabels()


# Used for SingleSideLogic
currentPlayer = 1


# Logic for server use
def singleSideLogic():
    global currentPlayer

    if not isBoardSolved() or not isBoardFull():
        printBoardWithLabels()
        if currentPlayer % 2 == 0:
            boardValues[getMove(playerTwoName)] = playerTwoMarker
        else:
            boardValues[getMove(playerOneName)] = playerOneMarker
        currentPlayer += 2
        printBoardWithLabels()

    if isBoardSolved():
        print("\n" * 100)
        currentPlayer -= 2
        if currentPlayer % 2 == 0:
            print(playerTwoName + " wins", end='')
        else:
            print(playerOneName + " wins", end='')
        print(" after " + str(math.ceil(currentPlayer / 2)) + " moves.")
        printBoardWithoutLabels()
        print("A total of " + str(currentPlayer) + " moves were made.")

    elif isBoardFull():
        print("Good game, nobody won this time.")

    else:
        print("Waiting on opponent...")


def instructions():
    temp = "Selections are made in the form of row column. To make a move in the top right corner, you would enter " + \
        "\'0 " + str(size - 1) + "\', without quotes.\n"
    temp += playerOneName + " will be using \'" + playerOneMarker + "\'; " + playerTwoName + " will be using \'" + \
        playerTwoMarker + "\'\n"
    return temp
