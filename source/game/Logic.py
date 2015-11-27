import Board as B
#logic of the game (Logic use the Board Class)
class Logic:

    #removes tile
    def removeTile(self, board, row, col):
        board.getBoard()[row][col] = 0 #sets board value at row, col to 0 (empty)
        return board

    #checks a column (columnNumber) for the number of empty spaces in it, returns number of empty spaces (numEmpty)
    def checkColumn(self, columnNumber, board):
        numEmpty = 0
        for i in range(0, 6):
            if board.getBoard()[i][columnNumber] == 0:
                numEmpty += 1
        return numEmpty

    #move tiles down to empty positions in a column (columnNumber)
    def moveDown(self, columnNumber, board, numEmpty):
        for i in range(5, numEmpty-1, -1):#checks each tile in column, starting with the bottom one, to the number of empty spaces
            if board.getBoard()[i][columnNumber] == 0:#if the tile is empty
                for j in range(i-1, -1, -1):#check each tile space in the column for a filled tile spaces
                    if board.getBoard()[j][columnNumber] != 0 :#if we find a filled tile
                        board.getBoard()[i][columnNumber] = board.getBoard()[j][columnNumber]#set the colour value of the current tile to the originally empty tile
                        board.getBoard()[j][columnNumber] = 0#the current tile is now empty
                        break

    #update the board with new tile position (after a turn) uses checkColumn and moveDown
    def addTile(self, board):
        for i in range(0, 6):
            numEmpty = Logic.checkColumn(i, board)#gets the number of empty spaces in each column
            if numEmpty != 0: #if there are empty tiles move the tiles into new postion
                 Logic.moveDown(i, board, numEmpty)
                 for j in range(0, numEmpty):
                    board.getBoard()[j][i] = B.T.Tile().getColor  #for the number of empty spaces in a column, replaces the corresponding number on the top of the column with a new tile object

    #checks if the colour of the tiles are the same
    def colourMatch(self, board, row, col, colour):
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

    #user input, enter a row and column to select the tiles you want to delete
    def userInput(self, board):
        countScore = 0
        contTurn = 'y'
        contGame = 'y'
        colour = -1
        tempRow = -1
        tempCol = -1
        board.printBoard()
        while contTurn == 'y':# while the user wishes to continue their turn 'y'
            row = int(input("Enter row: "))-1
            col = int(input("Enter column: "))-1
            contTurn = input("Continue turn?(y/n): ")
            if countScore > 1:#more the 2 tiles
                if Logic.adjacent(tempRow, tempCol, row, col) & Logic.colourMatch(board,row,col,colour):# if colours are the same, and the tiles are adjacent
                    tempRow = row #save the newly selected tile
                    tempCol = col
                    Logic.removeTile(board, row, col) #remove the newly selected tile
                    countScore += 1
            if countScore == 1:#on the second time around
                if Logic.adjacent(tempRow, tempCol, row, col) & Logic.colourMatch(board,row,col,colour):#if the colours are the same, and the tiles are adjacent
                    Logic.removeTile(board, tempRow, tempCol)#remove the first tile
                    tempRow = row # save the newly selected tile
                    tempCol = col
                    Logic.removeTile(board, row, col) #remove the second tile
                    countScore += 1
            if countScore == 0:#after the first selected when score is 0, we do not want to remove any tiles since we need to select 2+ tiles in order to remove them
                tempRow = row #save the initial row and col of the first tile
                tempCol = col
                colour = board.getBoard()[tempRow][tempCol]
                countScore += 1	
            board.printBoard()

        if contTurn == 'n': #if the user does not want to continue their turn
            Logic.addTile(board) #update the board with its new values
            board.printBoard()
            contGame = input("Continue game?(y/n): ") # asks the user if they want to continue game
            if contGame == 'y': # if the user wishes to continue game 'y', recursively use userInput with the current board state.
                Logic.userInput(board)
            else: #otherwise game ends
                print("GAME OVER")