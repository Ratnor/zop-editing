import Board as B

class Logic:

    def removeTile(board, row, col):
        board.getBoard()[row][col] = 0 #sets board value at row, col to 0 (empty)
        return board

    def checkColumn(columnNumber, board):
        numEmpty = 0
        for i in range(0, 6):
            if board.getBoard()[i][columnNumber] == 0:
                numEmpty += 1
        return numEmpty

    def moveDown(columnNumber, board, numEmpty):
        for i in range(5, numEmpty-1, -1):
            if board.getBoard()[i][columnNumber] == 0:
                for j in range(i-1, -1, -1):
                    if board.getBoard()[j][columnNumber] != 0 :
                        board.getBoard()[i][columnNumber] = board.getBoard()[j][columnNumber]
                        board.getBoard()[j][columnNumber] = 0
                        break

    def addTile(board):
        for i in range(0, 6):
            numEmpty = Logic.checkColumn(i, board)
            if numEmpty != 0:
                 Logic.moveDown(i, board, numEmpty)
                 for j in range(0, numEmpty):
                    board.getBoard()[j][i] = B.T.Tile().getColor()

    def colourMatch(board, row, col, colour):
        if board.getBoard()[row][col] == colour:
            return True
        else:
            return False

    def adjacent(row1, col1, row2, col2):
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
                newBoard = board
                Logic.userInput(newBoard)
            else:
                print("GAME OVER")