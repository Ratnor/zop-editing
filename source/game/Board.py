import Tile as T

#board class which initializes theg game board (Board use the Tile class)
class Board:
    #creates the board object
    def __init__(self):
        #board is initialized with a 6x6 array filled with tile objects of random colour
        self.board = [[T.Tile().getColor() for x in range(6)] for y in range(6)]

    #get the board array
    def getBoard(self):
        return self.board

    #prints the board in the console
    def printBoard(self):
        for i in range(0,6):
            for j in range(0,6):
                print(self.board[i][j], end = " ")
            print("")
        print("")

