from tile import Tile
class Board:
        board = []
        
        for row in range(6):
                board.append([])
                for column in range(6):
                        board[row].append(Tile)
	
        def pboard(board):
                for row in board:
                        print " ".join(row)

        
        
