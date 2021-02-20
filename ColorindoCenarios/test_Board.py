import unittest
from Board import Board
from colors import STANDARD_COLOR

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board_1 = Board(20, 20, 5, STANDARD_COLOR)
        self.board_2 = Board(-5, 20, 5, STANDARD_COLOR)
        self.board_3 = Board(20, -2, 5, STANDARD_COLOR)
        self.board_4 = Board(100, 100, 5, STANDARD_COLOR)

    def test_out_of_range(self):
        """Checking if out_of_range returns True (is out of range)
           or False (is in range).
        """
        self.assertFalse(Board.out_of_range(self.board_1,10,10))
        self.assertFalse(Board.out_of_range(self.board_4,99,99))
        self.assertTrue(Board.out_of_range(self.board_4,1000,50))
        self.assertTrue(Board.out_of_range(self.board_1,21,21))
        self.assertTrue(Board.out_of_range(self.board_2,10,10))
        self.assertTrue(Board.out_of_range(self.board_3,10,10))


if __name__ == '__main__':
    unittest.main()