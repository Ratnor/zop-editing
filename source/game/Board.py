import Tile as T

class Board:

    def __init__(self):
        self.board = [[T.Tile().getColor() for x in range(6)] for y in range(6)]

    def getBoard(self):
        return self.board

    def printBoard(self):
        for i in range(0,6):
            for j in range(0,6):
                print(self.board[i][j], end=" ")
            print("")
        print("")

