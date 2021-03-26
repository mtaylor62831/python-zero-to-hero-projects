def initialize():
    '''
    Sets or resets the tic-tac-toe game back to the beginning.
    The first player will always be X and the second is O
    '''
    global gameOver 
    gameOver = False
    global gameBoard 
    gameBoard = [[" "," "," "], [" "," "," "], [" "," "," "]]
    global player
    player = "Player 1"
    global symbol 
    symbol = "X"
    print("Let's play tic-tac-toe!")
    print("When it's your turn you will be prompted for a row and column to play in.")
    print("The game keeps track of who is X or O")
    print("Player 1 is first.")

def printBoard():
    for row in gameBoard:
        print(row)

def positionAllowed(inputPhrase):
    #verifies that the user inputs a valid row/column position
    val = input(inputPhrase)
    while val not in ["1", "2", "3"]:
        print("That is not a legal value. Try again")
        val = input(inputPhrase)
    return int(val)

def legalPlay(row, col):
    """
    Returns true if the player has selected an unoccipied space.
    REturns false if they need to play again
    """
    return gameBoard[row][col] == " "


initialize()

while not gameOver:
    row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3") - 1
    col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3") - 1

    while not legalPlay(row, col):
        print("Sorry, someone has already played in that spot. Pick a new one")
        row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3") - 1
        col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3") - 1

    #now we finally have a legal value! update the board and display it
    gameBoard[row][col] = symbol
    printBoard()
    #check if there is a winner
    currentCol = gameBoard[row][col] + gameBoard[row - 1][col] + gameBoard[row - 2][col]
    currentRow = gameBoard[row][col] + gameBoard[row][col -1] + gameBoard[row][col - 2]
    #still need to add case for the diagonal
    if currentCol == symbol*3 or currentRow == symbol*3:
        gameOver = True
        print(F"WOO HOO {player} has won the game!")
        #add something to ask if we want to play again
    #If there is no winner, swap the active player so we can take another turn    
    else:
        if player == "Player 1":
            player = "Player 2"
            symbol = "O"
        else:
            player = "Player 1"
            symbol = "X"