from unittest import TestCase
from Tile import Tile
from Board import Board
from Logic import Logic
__author__ = 'owner'


class TestTile(TestCase):
  def test_get_colour(self):
      t = Tile
      self.assertRaises(Exception, t.getColor,)

  def test_getBoard(self):
      b = Board
      self.assertRaises(Exception, b.getBoard, self)

  def test_initialization_Board(self):
      b_b = Board
      self.assertRaises(Exception, b_b.__init__, None)

  def test_removeTile(self):
      l = Logic
      b_c = Board
      self.assertRaises(Exception, l.removeTile, b_c, 2, 3)

  def test_checkColumn(self):
      l_b = Logic
      b_d = Board
      self.assertRaises(TypeError, l_b.checkColumn, "a", b_d)

  def test_move_down(self):
      l_c = Logic
      b_e = Board
      self.assertRaises(Exception, l_c.moveDown, 4, b_e, 2)

  def test_addTile(self):
      l_d = Logic
      b_f = Board
      self.assertRaises(Exception, l_d.addTile, b_f)

  def test_colourMatch(self):
      l_e = Logic
      b_g = Board
      t_a = Tile
      self.assertRaises(Exception, l_e.colourMatch, b_g, 2, 2, t_a.getColor)

  def test_adjacency(self):
      l_f = Logic
      self.assertRaises(Exception, l_f.adjacent, 2, 2, 0, 1)

  #def test_demo(self):
     # self.fail()

