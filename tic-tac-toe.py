def printBoard():
    for row in gameBoard:
        print(row)

def positionAllowed(inputPhrase):
    #verifies that the user inputs a valid row/column position
    val = input(inputPhrase)
    while val not in ["1", "2", "3"]:
        print("That is not a legal value. Try again")
        val = input(inputPhrase)
    return (int(val) - 1) #subtract 1 to get the right index

def legalPlay(row, col):
    """
    Returns true if the player has selected an unoccipied space.
    REturns false if they need to play again
    """
    return gameBoard[row][col] == " "

def playGame():
    '''
    This runs the functionality of the tic tac toe game.
    '''
    gameOver = False
    global gameBoard 
    gameBoard = [[" "," "," "], [" "," "," "], [" "," "," "]]
    player = "Player 1"
    symbol = "X"
    turn = 0
    print("Let's play tic-tac-toe!")
    print("When it's your turn you will be prompted for a row and column to play in.")
    print("The game keeps track of who is X or O")
    print("Player 1 is first.")
    while not gameOver:
        row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3")
        col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3")

        while not legalPlay(row, col):
            print("Sorry, someone has already played in that spot. Pick a new one")
            row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3")
            col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3")

        #now we finally have a legal value! update the board and display it
        gameBoard[row][col] = symbol
        printBoard()
        #check if there is a winner
        currentCol = gameBoard[0][col] + gameBoard[1][col] + gameBoard[2][col]
        currentRow = gameBoard[row][0] + gameBoard[row][1] + gameBoard[row][2]
        rightDiagonal = gameBoard[2][0] + gameBoard[1][1] + gameBoard[0][2]
        leftDiagonal = gameBoard[0][0] + gameBoard [1][1] + gameBoard[2][2]
        winVal = symbol*3
        turn += 1
        #still need to add case for the diagonal
        if winVal in [currentCol, currentRow, rightDiagonal, leftDiagonal]:
            gameOver = True
            print(F"WOO HOO {player} has won the game!")
            #add something to ask if we want to play again
        elif turn == 9:
            #if we are on turn 9 with no winner, the game is over.
            gameOver = True
            print("Both players made smart play. No winner is possible. Game over.")
        #If there is no winner, swap the active player so we can take another turn    
        else:
            if player == "Player 1":
                player = "Player 2"
                symbol = "O"
            else:
                player = "Player 1"
                symbol = "X"
    #check if the player wants to go again
    playAgain = input("Do you want to play again? Type y for Yes, type n for No")
    if playAgain in ["y", "Y"]:
        playGame()
    else:
        print("Thanks for playing! Enjoy the rest of your day")

    while not legalPlay(row, col):
        print("Sorry, someone has already played in that spot. Pick a new one")
        row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3") - 1
        col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3") - 1

playGame()
