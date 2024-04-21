import math
import random


class Node:
    def __init__(self, board_data):
        self.board_data = board_data

    # method to drwa the board according to the values of user and computer moves
    def drawBoard(self, user_sign):
        for i in range(3):
            for j in range(3):
                if self.board_data[i][j] == 0:
                    print("_", end=" ")
                elif self.board_data[i][j] == 1:
                    print("X", end=" ")
                elif self.board_data[i][j] == -1:
                    print("O", end=" ")
                elif self.board_data[i][j] == "X":
                    print(user_sign if user_sign == "X" else "O", end=" ")
                elif self.board_data[i][j] == "O":
                    print(user_sign if user_sign == "O" else "X", end=" ")
            print(end="\n")

    # method to check the valid and invalid according to the user input
    def isValidMove(self, number):
        if number < 0 or number > 9:
            return False
        else:
            row = (number - 1) // 3
            col = (number - 1) % 3
            if self.board_data[row][col] == 0:
                return True
            else:
                return False

    # method to set the move according to the player and updating the board
    def setMove(self, number, player):
        row = (number - 1) // 3
        col = (number - 1) % 3
        if self.isValidMove(number):
            if player == "O":
                self.board_data[row][col] = -1
            else:
                self.board_data[row][col] = 1
        else:
            print("This move is not passible")

    # method to check the player's win 
    def isWin(self, player):
        winList = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        mark = 1 if player == "X" else -1
        for indexes in winList:
            if (
                self.board_data[indexes[0] // 3][indexes[0] % 3]
                == self.board_data[indexes[1] // 3][indexes[1] % 3]
                == self.board_data[indexes[2] // 3][indexes[2] % 3]
                == mark
            ):
                return True
        return False

    # method to get the score according to the board values
    def getScore(self):
        if self.isWin("X"):
            return 1
        elif self.isWin("O"):
            return -1
        else:
            return 0

    # method to get the no of empty cells present in the board
    def getEmptyCell(self):
        emptyPosition = 0
        for i in range(3):
            for j in range(3):
                if self.board_data[i][j] == 0:
                    emptyPosition += 1
        return emptyPosition

    # method to check whether game over or not using getEmptyCell method
    def isGameOver(self):
        if self.getEmptyCell() > 0:
            return False
        else:
            return True


class TicTacToe:
    def __init__(self):
        self.board = Node([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    # minimax algorithm
    def minimax(self, state, depth, player):
        if player == "X":
            best = [-1, -math.inf]
        else:
            best = [-1, math.inf]

        if depth == 0 or state.isGameOver():
            score = state.getScore()
            return [-1, score]

        emptyCells = state.getEmptyCell()

        for cell in range(1, 10):
            if state.isValidMove(cell):
                state.setMove(cell, player)
                if player == "X":
                    score = self.minimax(state, depth - 1, "O")
                else:
                    score = self.minimax(state, depth - 1, "X")
                state.board_data[(cell - 1) // 3][(cell - 1) % 3] = 0
                score[0] = cell

                if player == "X": 
                    if score[1] > best[1]:
                        best = score
                else:
                    if score[1] < best[1]:
                        best = score
        return best

    # method for move of computer and checking all the possible things
    def computerMove(self, user_sign):
        depth = self.board.getEmptyCell()
        if depth == 0 or self.board.isGameOver():
            return

        print("Computer's turn:")
        move = self.minimax(self.board, depth, "X")[0]
        self.board.setMove(move, "O" if user_sign == "X" else "X")
        self.board.drawBoard(user_sign)  # Display the board after the computer's move
        print("------------------")

        if self.board.isWin("O" if user_sign == "X" else "X"):
            print("Computer wins!")
            return True  # Return True if the game is over
        elif self.board.isGameOver():
            print("It's a tie!")
            return True
        return False

    # method for move of player and checking all the possible things
    def playerMove(self, user_sign):
        if self.board.isGameOver():
            return

        print("Player's turn:")
        while True:
            move = input("Enter your move (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9:
                move = int(move)
                if self.board.isValidMove(move):
                    self.board.setMove(move, user_sign)
                    self.board.drawBoard(user_sign)  # Display the board after the player's move
                    print("------------------")

                    if self.board.isWin(user_sign):
                        print("Congratulations! You win!")
                        return True  # Return True if the game is over
                    elif self.board.isGameOver():
                        print("It's a tie!")
                        return True
                    break
                else:
                    print("That position is already occupied. Please choose another position.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        return False

    # method to start the game and call all the method from TicTacToe class
    def startGame(self):
        print("------------------")
        self.board.drawBoard(
            ""
        )  # Display the initial board without the user's chosen sign
        # Randomly decide who starts first
        print("------------------")
        first_turn = random.choice(["user", "computer"])
        print("First turn:", first_turn)

        # Allow the user to choose their sign
        user_sign = input("Choose your sign (X or O): ").upper()
        while user_sign not in ["X", "O"]:
            user_sign = input("Invalid input. Choose your sign (X or O): ").upper()
        print("------------------")
        while True:
            if first_turn == "user":
                if self.playerMove(user_sign):
                    break
                if self.computerMove(user_sign):
                    break

            else:
                if self.computerMove(user_sign):
                    break
                if self.playerMove(user_sign):
                    break


def test():
    print("-------------------")
    print("22012012001 - Barot Dhruv Dineshbhai")
    game = TicTacToe()
    game.startGame()

test()
