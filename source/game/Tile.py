import random
#tile class which contains the value of each tile
class Tile:

    #create a tile object
    def __init__(self):
        #possible colours of each tile
        color = ["R","B","G","P","Y"]
        #randomly choose one colour
        self.color = random.choice(color)

    #gets the tile's colour
    def getColor(self):
        return self.color


