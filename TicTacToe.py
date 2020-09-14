#TicTacToe.py
import random

import BoardFunctions



class Player:

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return "<Player Class: name = \'"+self.name+"\'>"

    def getPlayerMove(self, board):

        move = '0'

        while move not in '1 2 3 4 5 6 7 8 9'.split() or not BoardFunctions.isSpaceFree(board, int(move)):

            print(self.name+', What is your next move? (1-9)')

            move = input()

        return int(move)



    def makeMove(self, board, letter, move):

        board[move] = letter



def inputPlayerLetter():

    letter = ''

    while not (letter == 'X' or letter == 'O'):

        print('Player One, Do you want to be X or O?')

        letter = input().upper()



    if letter == 'X':

        print("Player Two is O\n")

        return ['X', 'O']

    else:

        print("Player Two is X\n")

        return ['O', 'X']



def whoGoesFirst():

    # Randomly choose the Player who goes first.

    if random.randint(0, 1) == 0:

        return 'PlayerTwo'

    else:

        return 'PlayerOne'





def playAgain():

    print('Do you want to play again? (yes or no)')

    return input().lower().startswith('y')



print('Welcome to Tic Tac Toe!')

# Reset the board

while True:

    theBoard = [' '] * 10

    PlayerOneLetter, PlayerTwoLetter = inputPlayerLetter()

    turn = whoGoesFirst()

    print('The ' + turn + ' will go first.')

    gameIsPlaying = True

    PlayerOne = Player('PlayerOne')

    PlayerTwo = Player('PlayerTwo')



    # Player’s turn.

    while gameIsPlaying:

        if turn == 'PlayerOne':

            # Player One's turn.

            BoardFunctions.drawBoard(theBoard)

            move = PlayerOne.getPlayerMove(theBoard)

            PlayerOne.makeMove(theBoard, PlayerOneLetter, move)

            if BoardFunctions.isWinner(theBoard, PlayerOneLetter):

                BoardFunctions.drawBoard(theBoard)

                print(PlayerOne.name + ' won!')

                gameIsPlaying = False

            else:

                if BoardFunctions.isBoardFull(theBoard):

                    BoardFunctions.drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'PlayerTwo'



        else:

            # Player Two's turn.

            BoardFunctions.drawBoard(theBoard)

            move = PlayerTwo.getPlayerMove(theBoard)

            PlayerTwo.makeMove(theBoard, PlayerTwoLetter, move)



            if BoardFunctions.isWinner(theBoard, PlayerTwoLetter):

                BoardFunctions.drawBoard(theBoard)

                print(PlayerTwo.name + ' won!')

                gameIsPlaying = False

            else:

                if BoardFunctions.isBoardFull(theBoard):

                    BoardFunctions.drawBoard(theBoard)

                    print('The game is a tie!')

                    break

                else:

                    turn = 'PlayerOne'



    if not playAgain():

        break
