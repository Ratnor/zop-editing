
import Logic as L

class Main:
    """This class is the basis
    for initializing the game
    with a proper board and logic.
    
    Input(s): None for this module.
    Output(s): None for this module.

    State variables: None for this module.
    Environment variables: None for this module.

    Exceptions: None for this module.
    """
    logic = L.Logic
    board = L.B.Board() 
    logic.userInput(board) 



