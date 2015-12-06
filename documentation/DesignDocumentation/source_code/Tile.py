import random


class Tile:
    """Class for representing and creating
    tiles to populate the board with.

    __init__: Input:
    Function requires a parameter.
    Output:
    Function will initialize a tile of random color.

    getColor: Input:
    Function requires a parameter.
    Output:
    Function will return tile's color.

    State variables:
    self (for __init__): refers to newly created object
    self (for getColor): refers to instance whose method was called


    Environment variables: None for this module.

    Exceptions: None for this module."""

    def __init__(self):
        """Constructor method for
        setting a random color to a tile.
        """
        
        color = ["R","B","G","P","Y"]
        self.color = random.choice(color)

    
    def getColor(self):
        """Getter method for tile color."""
        return self.color


