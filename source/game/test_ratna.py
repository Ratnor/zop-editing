from Logic import *
from Board import *
import unittest

# sample board with the colour red
allTile = Board()
for x in range(6):
    for y in range(6):
        allTile.getBoard()[x][y] = 'R'

# sample board with color red and missing a piece at 2,3 (x,y).
missingTile = Board()
for x in range(6):
    for y in range(6):
        missingTile.getBoard()[x][y] = 'R'
missingTile.getBoard()[2][3] = 0

#Test class
class Test_Logic(unittest.TestCase):


# Tests the first function in Logic
#   Checks if remove tile by passing a full board and the same board with a missing piece.
    def test_removeTile(self):
        print (str(missingTile))
        print (allTile)
        self.assertEqual(str(Logic.removeTile(allTile,2,3)), str(missingTile))
        self.assertNotEqual(str(Logic.removeTile(allTile,5,5)), str(missingTile))



#main to run the tests
if __name__ == '__main__':
    unittest.main()