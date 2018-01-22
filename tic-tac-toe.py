import random

def drawBoard(board):
    print('   I   I')
    print(" " + board[7] + ' I ' + board[8] + ' I ' + board[9])
    print('   I   I')
    print('-----------')
    print('   I   I')
    print(" " + board[4] + ' I ' + board[5] + ' I ' + board[6])
    print('   I   I')
    print('-----------')
    print('   I   I')
    print(" " + board[1] + ' I ' + board[2] + ' I ' + board[3])
    print('   I   I')

def inputPlayerLetter():
    letter = ''
    while not(letter == 'X' or letter == "O"):
        print("Do you want to be X or O")
        letter = input().upper()

    if letter == 'X':
        return ["X","O"]
    else:
        return ["O", "X"]

def whoGoesFirst():
    if random.randint(0, 1)==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print("Do you want to play again")
    return input().lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo, le):
    return((bo[7]== le and bo[8] == le and bo[9] == le) or # across the top
           (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
           (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
           (bo[7] == le and bo[4] == le and bo[1] == le) or  # across the left side
           (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
           (bo[9] == le and bo[6] == le and bo[3] == le) or
           (bo[7] == le and bo[5] == le and bo[3] == le) or
           (bo[9] == le and bo[5] == le and bo[1] == le))
def getBoardCopy(board):
    dupeboard = []

    for i in board:
        dupeboard.append(i)

    return dupeboard

def isSpaceFree(board, move):

    return board[move] == ' '

def getPlayerMove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move!= None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
