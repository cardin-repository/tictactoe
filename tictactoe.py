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
#implement an easier way to check for win instead of repeating code, maybe a combo list
def winHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = currentPlayer
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = currentPlayer
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = currentPlayer
        return True
    
def winVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = currentPlayer
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = currentPlayer
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = currentPlayer
        return True
    
def winDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = currentPlayer
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = currentPlayer
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        gameBoard(board)
        print("Tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if winDiagonal(board) or winHorizontal(board) or winVertical(board):
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