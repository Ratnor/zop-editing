import Tile as T

class Logic: 
        
    def userInput():       
        coord = []

        n = int(input("how many tiles would you like to select? "))            #coordinate count
        xArray = [0]*n  #array to hold the x-coordinates
        yArray = [0]*n  #array to hold the y-coordinates
        
        for i in range(n):
            print (i)
            xArray[i] = int(input("Enter X: "))
            yArray[i] = int(input("Enter Y: "))

            coord = list(zip(xArray, yArray))

        return coord

    
# Check if the pieces are in line {add to function.docx}


    def colorMatch(coord, Board, color):
        xArray = []
        yArray = []
        for i in range(len(coord)):
            tupple = coord[i]
            xArray.append(tupple[0])        # x: array with all the x-coordinates
            yArray.append(tupple[1])        # y: array with all the y-coordinates

        for x in range(len(Board)):
            for y in range (len(Board)):
                if (Board[x][y].getColor() == color):
                    return True
                else:
                    return False
  
    def score(tilesRemoved):
        return tilesRemoved
def main():
##    board = [[T.Tile(x,y).getColor() for x in range(6)] for y in range(6)]
##    for i in range(0,6):
##        for j in range(0,6):
##            print(board[i][j], end =" ")
##    print("")

    print (Logic.userInput())
##    print (Logic.score(3))
    
