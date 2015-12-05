import Tile as T


class Board:
    """Board class initializes the game board (Board uses the Tile class).

    __init__: Input:
    Function requires a parameter.
    Output:
    Function will initialize a 6x6 board with tiles.

    getBoard: Input:
    Function requires a parameter.
    Output:
    Function will return a board.

    printBoard: Input:
    Function requires a parameter.
    Output:
    Function will print a working board.

    State variables:
    self (for __init__): refers to newly created object
    self (for getBoard): refers to instance whose method was called
    self (for printBoard): refers to instance whose method was called.

    Environment variables: None for this module.

    Exceptions: None for this module.
    """
    
    def __init__(self):
        """Constructor for Board.

        Constructs a 6x6 board with tiles of random colours.
        """
        self.board = [[T.Tile().getColor() for x in range(6)] for y in range(6)]

    
    def getBoard(self):
        """Getter method for Board.

        """
        return self.board

    
    def printBoard(self):
        """Method for printing the Board.

        """
        for i in range(0,6):
            for j in range(0,6):
                print(self.board[i][j], end=" ")
            print("")
        print("")

