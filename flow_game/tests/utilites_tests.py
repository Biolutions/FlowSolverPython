import unittest
from flow_game import utilities
from flow_game import flow_board

TEST_PATH = "../../TestBoards/"


class TestFlowUtilities(unittest.TestCase):
    def test_equal_boards(self):
        board1 = [['0', 'R', 'B'], ['R', 'B', '0']]
        board2 = [['0', 'R', 'B'], ['R', 'B', '0']]
        board3 = [['0', 'R', 'B'], ['0', 'R', 'B']]

        self.assertTrue(utilities.equal_boards(board1, board2), "Two boards that are the same")
        self.assertFalse(utilities.equal_boards(board1, board3), "Second board differs in one position")

    def test_load_game(self):
        expected_board = [['R', '0', 'G', '0', 'Y'],
                         ['0', '0', 'B', '0', 'O'],
                         ['0', '0', '0', '0', '0'],
                         ['0', 'G', '0', 'Y', '0'],
                         ['0', 'R', 'B', 'O', '0']]

        loaded_game = utilities.load_game(TEST_PATH + "easy5x5.txt")
        self.assertTrue(utilities.equal_boards(loaded_game.get_board_copy(), expected_board))

    def test_at_goal(self):
        test_board = [['0', 'R', '0'],
                      ['R', '0', '0']]

        flow_game = flow_board.Flow(test_board)
        self.assertFalse(utilities.at_goal(flow_game))
        flow_game.paths['R'].add_to_path((0, 0))
        self.assertTrue(utilities.at_goal(flow_game))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlowUtilities)
    unittest.TextTestRunner(verbosity=2).run(suite)










