import random
class Tile:

    def __init__(self):
        color = ["R","B","G","P","Y"]
        self.color = random.choice(color)

    def getColor(self):
        return self.color


