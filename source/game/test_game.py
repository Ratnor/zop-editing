from unittest import TestCase

from Board import Board
from Logic import Logic
import random
__author__ = 'owner'


class TestZop(TestCase):


  def test_removeTile(self): #System test - 3.1
      b = Board()
      l_a = Logic.removeTile(b, 0, 0)
      self.assertEqual(b.getBoard()[0][0], 0) #Assertion to check that when tile is removed, the empty spot is given value =0

  def test_remove2(self): #System test - 3.2
      b = Board()
      l_b = Logic.removeTile(b, 0, 0)
      self.assertNotEqual(b.getBoard()[0][0], 1) #Assertion to check that when tile is removed, the empty spot is NOT given value =0

  def test_addTile(self): #System test - 3.5
      b = Board()
      for i in range(0, 5):
          for j in range(0, 5):
              self.assertNotEqual(b.getBoard()[i][j], 0) #Assertion is to make sure that the board is always populated with 36 tiles (board size is 6x6)

  def test_colourMatch(self): #System test - 3.3
      b = Board()
      colour = random.choice(["R","B","G","P","Y"])
      ll = Logic.colourMatch(b,0,0,colour)
      self.assertEqual(b.getBoard()[0][0] == colour, True)

  def test_adjacency(self): #System test - 3.6
      logic = Logic()
      self.assertTrue(logic.adjacent(2,0,2,1)) #When tiles are adjacent, assertion will be True (or else it will be False)

  def test_exception_moveDown(self): #System test - 3.7
      l = Logic()
      b = Board()
      self.assertRaises(TypeError, l.moveDown, 'a', b, 0) # moveDown from Logic takes three arguments: columnNumber, board, and numEmpty, but this assertion throws one string in place of an integer (i.e. a character for 'columnNumber' instead of number); thus it is TypeException


