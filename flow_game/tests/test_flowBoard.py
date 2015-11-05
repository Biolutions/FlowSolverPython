from unittest import TestCase
from flow_game.flow_board import Flow
import flow_game.utilities as utilities
import unittest

__author__ = 'nick'


class TestFlowBoard(TestCase):

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


if __name__ == '__main__':
    unittest.makeSuite(TestFlowBoard).run()
