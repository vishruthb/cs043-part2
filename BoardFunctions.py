#BoardFunctions.py

def drawBoard(board):

    # This function prints out the board that it was passed.



    # "board" is a list of 10 strings representing the board (ignore index 0)

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')



# Given a board and a player’s letter, this function returns True if that player has won.

# We use bo instead of board and le instead of letter so we don’t have to type as much.

def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top

    (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle

    (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom

    (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side

    (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle

    (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side

    (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal

    (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal



def isSpaceFree(board, move):

    return board[move] == ' '



def isBoardFull(board):

    for i in range(1,10):

        if isSpaceFree(board,i):

            return False

    return True

