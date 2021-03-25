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

initialize()

row = positionAllowed(F"{player} what row would you like to play in? Pick a value 1,2 or 3") - 1
col = positionAllowed(F"{player} which column would you like to play in? Pick a value 1,2 or 3") - 1
#check to make sure that space is blank
if gameBoard[row][col] == " ":
    gameBoard[row][col] = symbol
else:
    print("Sorry, someone has already played in that spot. Pick a new one")
printBoard()




