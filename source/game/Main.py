
import Logic as L
#Main class, runs the game. (Main uses the Logic class)
class Main:

    logic = L.Logic
    board = L.B.Board() #initialize board
    logic.userInput(board) #run the game using board.



