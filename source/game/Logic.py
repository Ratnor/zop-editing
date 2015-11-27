import Board as B

#logic of the game (Logic use the Board Class)
class Logic:

    #removes tile
    @classmethod
    def removeTile(cls, board, row, col):
        board.getBoard()[row][col] = 0 #sets board value at row, col to 0 (empty)
        return board

    #checks a column (columnNumber) for the number of empty spaces in it, returns number of empty spaces (numEmpty)
    @classmethod
    def checkColumn(cls, columnNumber, board):
        numEmpty = 0
        for i in range(0, 6):
            if board.getBoard()[i][columnNumber] == 0:
                numEmpty += 1
        return numEmpty

    #move tiles down to empty positions in a column (columnNumber)
    @classmethod
    def moveDown(cls, columnNumber, board, numEmpty):
        for i in range(5, numEmpty-1, -1):#checks each tile in column, starting with the bottom one, to the number of empty spaces
            if board.getBoard()[i][columnNumber] == 0:#if the tile is empty
                for j in range(i-1, -1, -1):#check each tile space in the column for a filled tile spaces
                    if board.getBoard()[j][columnNumber] != 0 :#if we find a filled tile
                        board.getBoard()[i][columnNumber] = board.getBoard()[j][columnNumber]#set the colour value of the current tile to the originally empty tile
                        board.getBoard()[j][columnNumber] = 0#the current tile is now empty
                        break

    #update the board with new tile position (after a turn) uses checkColumn and moveDown
    @classmethod
    def addTile(cls, board):
        for i in range(0, 6):
            numEmpty = Logic.checkColumn(i, board)#gets the number of empty spaces in each column
            if numEmpty != 0: #if there are empty tiles move the tiles into new postion
                 Logic.moveDown(i, board, numEmpty)
                 for j in range(0, numEmpty):
                    board.getBoard()[j][i] = B.T.Tile().getColor  #for the number of empty spaces in a column, replaces the corresponding number on the top of the column with a new tile object

    #checks if the colour of the tiles are the same
    @classmethod
    def colourMatch(cls, board, row, col, colour):
        if board.getBoard()[row][col] == colour:
            return True
        else:
            return False

    #checks if the newly selected tile, is adjacent to the currently selected one
    def adjacent(self, row1, col1, row2, col2):
        if row1 == row2:
            if (col1 == col2+1) | (col1 == col2-1):
                return True
            else:
                return False
        elif col1 == col2:
            if (row1 == row2+1) | (row1 == row2-1):
                return True
            else:
                return False
        else:
            return False

