boardValues = [['.' for x in range(8)] for y in range(5)]
diagonalValues = [['.' for x in range(5)] for y in range(8)]
players = [[0, 'X'], [0, 'O']]        #Stores discord IDs of the player in each room.
playerMarker = 'X'

#RECODE TO CHECK FOR A MATCH ONLY AROUND CHANGED PIECES.
#If only one piece has been dropped, just do a check around those.
#If a flip has been made, check the entire board.

def storePlayers(playerID):
    if(players[0] != 0):
        players[1] = playerID

    else:
        players[0] = playerID
    return None;

def clearRoom():
    players = [0, 0]
    for i in range(0, 8):
        for j in range(0, 5):
            boardValues[j][i] = '.'
            diagonalValues[i][j] = '.'
    playerMarker = 'X'
    return None;

def winCheck():
    isWin = False
    checkNotDone = True
    u = 0
    v = 0
    w = 0

    while(checkNotDone & u < 8):
        if (boardValues[0][u] != '.' & boardValues[0][u] == boardValues[1][u] & boardValues[2][u] == boardValues[3][u] & boardValues[3][u] == boardValues[4][u] & boardValues[4][u] == boardValues[0][u]):
            isWin = True
            checkNotDone = False
        u += 1

    if(checkNotDone):
        while(checkNotDone & v < 5):
            counter = 0
            i = 0

            while(i < 7 & counter < 5):
                if (boardValues[v][i] == boardValues[v][i+1] & boardValues[v][i] != '.'):
                    counter += 1

                else:
                    counter = 0

                if(counter == 4):
                    isWin = True
                    checkNotDone = False
                i += 1
            v += 1

            if(checkNotDone):
                while(checkNotDone & w < 8):
                    if(diagonalValues[w][0] != '.' & diagonalValues[w][0] == diagonalValues[w][1] & diagonalValues[w][2] == diagonalValues[w][3] & diagonalValues[w][3] == diagonalValues[w][4] & diagonalValues[w][4] == diagonalValues[w][0]):
                        isWin = True
                        checkNotDone = False
    return isWin;

def storeDiagonals():
    for i in range(0, 4):
        for j in range(0, 5):
            diagonalValues[i][j] = boardValues[j][j + 1]
    counter = 0

    for i in range(4, 8):
        for j in range(0, 5):
            diagonalValues[i][j] = boardValues[j][7 - j - counter]
        counter += 1
    return None;

def verifyPlayer(playerInputID):
    if(playerMarker == 'X' & players[0][0] == playerInputID):
        return True;

    elif(playerMarker == 'O' & players[1][0] == playerInputID):
        return True;

    else:
        return False;

def generateBoardValues(userChoice):    #Generates and changes the board.
    returnValue = True

    if(userChoice == 'r' | userChoice == 'R'):        #Runs if a user chooses to swap values.
        for i in range(0, 5):                            #Runs through each column.
            if(boardValues[i][6] != '.'):                      #Executes row swaps only if the column has at least two filled spaces to work with.
                indexOfTopValue = 8                     #Stores index of the topmost value in the column.
                l = 0

                while(indexOfTopValue == 8):                                        #Locates the topmost non-empty value in the column.
                    if(boardValues[i][l] != '.'):
                        indexOfTopValue = l
                    l += 1              #Runs until it finds a non-empty value.
                bottomValue = boardValues[i][7]

                for j in range(7, indexOfTopValue, -1):       #Shifts every value in the column down.
                    boardValues[i][j] = boardValues[i][j - 1]
                boardValues[i][indexOfTopValue] = bottomValue  #Places the previous bottom value at the top of the column.

    elif (48 < int(userChoice) & int(userChoice) < 54):
        userChoiceNum = int(userChoice) - 49

        if(boardValues[userChoiceNum][0] == '.'):  #Checks if the selected row is not full.
            isNotDropped = True
            i = 0

            while(isNotDropped):                                   #Checks for topmost blank value and drops one in.
                if(boardValues[userChoiceNum][i] != '.' | i == 8):
                    boardValues[userChoiceNum][i-1] = playerMarker
                    isNotDropped = False

                else:
                    i += 1

        else:                                #Runs if the selected row is full.
            print("Choose another column because you picked a full one.\n")
            returnValue = False

    else:                                      #Error message if the user doesn't enter a valid command.
        print("Invalid input. Try something else.\n")
        returnValue = False
    return returnValue;

def gameSet():
    #How to accept playerID values and run
    if(players[0][0] != 0 & players[1][0] != 0):
        print("placeholder. run game once values are accepted.")

    return None;