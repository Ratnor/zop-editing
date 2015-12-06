import Board as B

class Logic:
    """This class is responsible for
    the logic behind the game.

    removeTile: Input:
    Function requires three parameters.
    Output:
    Function will remove tile in the given position.

    checkColumn: Input:
    Function requires two parameters.
    Output:
    Function will return number of empty spaces in a column.

    moveDown: Input:
    Function requires three parameters.
    Output:
    Function will move tiles down to empty positions in a column.

    addTile: Input:
    Function requires a parameter.
    Output:
    Function will add tile(s) to empty positions; this function uses checkColumn and moveDown methods.

    colourMatch: Input:
    Function requires four parameters.
    Output:
    Function will see if selected tiles are of the same colour or not (boolean).

    adjacent: Input:
    Function requires four parameters.
    Output:
    Function will see if selected tiles are adjacent to each other or not (boolean).

    userInput: Input:
    Function requires a parameter.
    Output:
    Function will make the board respond to user input.

    State variables:
    board: used by all, but one method in this module (adjacent does not need to use board)
    row: represents a row on the board
    col: represents a column on the board
    columnNumber: refers to one column (out of 6) on the board
    numEmpty: refers to the count of empty positions in a column
    colour: refers to colour of a tile
    row1 and row2: refer to any two rows on board
    col1 and col2: refer to any two columns on the board

    Environment variables:
    row (in userInput method): based on user interaction with keyboard; user has to enter row number
    col (in userInput method): user has to enter column number
    contTurn (in userInput method): user can decide to continue with game or quit

    Exceptions:
    row (in userInput method): row number entered out of range
        Row number has to be between 1 and 6
        
    col (in userInput method): column number entered out of range
        Column number has to be between 1 and 6
        
    contTurn (in userInput method): character entered invalid
        Character entered has to be 'y' or 'n'
    """
    def removeTile(board, row, col):
        """Method for removing
        a tile (in the case where tiles of same
        color are matched)."""
        board.getBoard()[row][col] = 0 
        return board

    
    def checkColumn(columnNumber, board):
        """Method for checking empty
        spaces in a column."""
        numEmpty = 0
        for i in range(0, 6):
            if board.getBoard()[i][columnNumber] == 0:
                numEmpty += 1
        return numEmpty

   
    def moveDown(columnNumber, board, numEmpty):
        """Method for moving tiles down
        to empty positions in a given column."""
        for i in range(5, numEmpty-1, -1):
            if board.getBoard()[i][columnNumber] == 0:
                for j in range(i-1, -1, -1):
                    if board.getBoard()[j][columnNumber] != 0 :
                        board.getBoard()[i][columnNumber] = board.getBoard()[j][columnNumber]
                        board.getBoard()[j][columnNumber] = 0
                        break


    def addTile(board):
        """Method for adding tile(s)
        in empty position(s). This method
        uses checkColumn and
        moveDown methods as well."""
        for i in range(0, 6):
            numEmpty = Logic.checkColumn(i, board)
            if numEmpty != 0: 
                 Logic.moveDown(i, board, numEmpty)
                 for j in range(0, numEmpty):
                    board.getBoard()[j][i] = B.T.Tile().getColor()

    #checks if the colour of the tiles are the same
    def colourMatch(board, row, col, colour):
        """Method to check if the color
        of tiles is the same or not (when trying to match)."""
        if board.getBoard()[row][col] == colour:
            return True
        else:
            return False

  
    def adjacent(row1, col1, row2, col2):
        """Method to check whether
        the newly selected tile is
        adjacent or not to the
        currently selected one."""
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

    
    def userInput(board):
        """Method for all possible
        inputs that user can give
        to board. Two important
        actions include deleting
        tiles by entering row(s) and
        column(s), and continuing
        with/ending the game."""
        countScore = 0
        contTurn = 'y'
        contGame = 'y'
        colour = -1
        tempRow = -1
        tempCol = -1
        board.printBoard()
        while contTurn == 'y':
            row = int(input("Enter row: "))-1
            col = int(input("Enter column: "))-1
            contTurn = input("Continue turn?(y/n): ")
            if countScore > 1:
                if Logic.adjacent(tempRow, tempCol, row, col) & Logic.colourMatch(board,row,col,colour):
                    tempRow = row 
                    tempCol = col
                    Logic.removeTile(board, row, col) 
                    countScore += 1
            if countScore == 1:
                if Logic.adjacent(tempRow, tempCol, row, col) & Logic.colourMatch(board,row,col,colour):
                    Logic.removeTile(board, tempRow, tempCol)
                    tempRow = row 
                    tempCol = col
                    Logic.removeTile(board, row, col) 
                    countScore += 1
            if countScore == 0:
                tempRow = row 
                tempCol = col
                colour = board.getBoard()[tempRow][tempCol]
                countScore += 1
            board.printBoard()

        if contTurn == 'n': 
            Logic.addTile(board) 
            board.printBoard()
            contGame = input("Continue game?(y/n): ") 
            if contGame == 'y': 
                Logic.userInput(board)
            else: 
                print("GAME OVER")
