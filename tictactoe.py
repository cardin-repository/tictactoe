#basic vars
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True



#print game board
def gameBoard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

#get player input
def playerInput(board):
    pInput = int(input("Choose a square 1-9: "))
    if pInput >= 1 and pInput <= 9 and board[pInput-1] == "-":
        board[pInput-1] = currentPlayer
    else:
        print("Player is in spot or invalid input")

#check for win or tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        gameBoard(board)
        print("Tie!")
        gameRunning = False

def checkWin():
    global winner, gameRunning
    winningCombinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
        (0, 4, 8), (2, 4, 6)              # diagonal
    ]
    #iterate through the winning combbinations to determine winner instead of manual checking, useful for if larger boards or rule adjustment
    for combo in winningCombinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "-":
            winner = currentPlayer
            gameBoard(board)
            print(f"The winner is {winner}")
            gameRunning = False
        

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again

while gameRunning:
    gameBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()