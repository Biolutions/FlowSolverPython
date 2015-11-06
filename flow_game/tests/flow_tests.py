from unittest import TestCase
from flow_game.flow_board import Flow, Path
import flow_game.utilities as utilities
import unittest

__author__ = 'nick'

TEST_PATH = "../../TestBoards/"


class TestFlow(TestCase):
    def setUp(self):
        self.simple_board = [['R', 'O', '0'],
                             ['0', '0', '0'],
                             ['R', '0', 'O']]

    def test_get_board_copy(self):
        test_board = [['0', 'R', '0'],
                      ['R', '0', '0']]

        flow = Flow(test_board)
        original_board = flow.get_board_copy()
        self.assertTrue(utilities.equal_boards(test_board, original_board),
                        "Returned board should be the same as the test board")

        original_board[0][0] = 'T'
        self.assertFalse(utilities.equal_boards(test_board, original_board),
                         "Change made to the returned board. Test board should not be the same as it")

        self.assertTrue(utilities.equal_boards(test_board, flow.get_board_copy()),
                        "Change made to the returned board should not effect the new copy")

    def test_find_end_points(self):
        testFlow = utilities.load_game(TEST_PATH + "easy5x5.txt")
        self.assertTrue((0, 0) in testFlow._end_points['R'],
                        "There is a R end point at position 0, 0 (row, col) in easy5x5.txt")

        self.assertTrue((3, 3) in testFlow._end_points['Y'],
                        "There is a Y end point at position 3, 3 (row, col) in easy5x5.txt")

    def test_is_valid(self):
        flow_instance = utilities.load_game(TEST_PATH + "easy5x5.txt")

        self.assertFalse(flow_instance.is_valid(-1, 0), "Negative row value test")
        self.assertFalse(flow_instance.is_valid(0, 5), "5x5 grid only has values up to index 4. (0,5) is invalid")
        self.assertTrue(flow_instance.is_valid(4, 4), "(4, 4) last valid position in 5x5 Grid")

    def test_is_empty(self):
        flow_instance = utilities.load_game(TEST_PATH + "easy5x5.txt")

        self.assertFalse(flow_instance.is_empty(0, 0))
        self.assertTrue(flow_instance.is_empty(0, 1))

    def test_adjacent_points(self):
        test_game = Flow(self.simple_board)
        self.assertTrue(test_game.adjacent_points((1, 0), (2, 0)))
        self.assertTrue(test_game.adjacent_points((2, 0), (1, 0)))

        self.assertFalse(test_game.adjacent_points((0, 3), (0, 2)))
        self.assertFalse(test_game.adjacent_points((0, 0), (1, 1)))


class TestPath(TestCase):
    def setUp(self):
        self.simple_board = [['R', 'O', '0'],
                             ['0', '0', '0'],
                             ['R', '0', 'O']]


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlow)
    unittest.TextTestRunner(verbosity=2).run(suite)
