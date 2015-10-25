import random
class Tile:

    def __init__(self,x,y):
        color = ["R","B","G","P","Y"]
        self.x = x
        self.y = y
        self.color = random.choice(color)

    def getColor(self):
        return self.color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

