from unittest import TestCase
from flow_game.flow_board import Flow
import flow_game.utilities as utils
import copy
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
        self.assertTrue(utils.equal_boards(test_board, original_board),
                        "Returned board should be the same as the test board")

        original_board[0][0] = 'T'
        self.assertFalse(utils.equal_boards(test_board, original_board),
                         "Change made to the returned board. Test board should not be the same as it")

        self.assertTrue(utils.equal_boards(test_board, flow.get_board_copy()),
                        "Change made to the returned board should not effect the new copy")

    def test_find_end_points(self):
        test_flow = Flow(self.simple_board)
        red_path = test_flow.paths['R'].path_from1
        red_path += test_flow.paths['R'].path_from2
        orange_path = test_flow.paths['O'].path_from1
        orange_path += test_flow.paths['O'].path_from2

        self.assertTrue((0, 0) in red_path,
                        "There is a R end point at position 0, 0 in simple board")

        self.assertTrue((2, 2) in orange_path,
                        "There is a O end point at 2,2 in simple board")

    def test_is_valid(self):
        flow_instance = utils.load_game(TEST_PATH + "easy5x5.txt")

        self.assertFalse(flow_instance.is_valid(-1, 0), "Negative row value test")
        self.assertFalse(flow_instance.is_valid(0, 5), "5x5 grid only has values up to index 4. (0,5) is invalid")
        self.assertTrue(flow_instance.is_valid(4, 4), "(4, 4) last valid position in 5x5 Grid")

    def test_is_empty(self):
        flow_instance = utils.load_game(TEST_PATH + "easy5x5.txt")

        self.assertFalse(flow_instance.is_empty(0, 0))
        self.assertTrue(flow_instance.is_empty(0, 1))

    def test_adjacent_points(self):
        test_game = Flow(self.simple_board)
        self.assertTrue(test_game.adjacent_points((1, 0), (2, 0)))
        self.assertTrue(test_game.adjacent_points((2, 0), (1, 0)))

        self.assertFalse(test_game.adjacent_points((0, 3), (0, 2)))
        self.assertFalse(test_game.adjacent_points((0, 0), (1, 1)))

    def test_equals(self):
        game1 = Flow(self.simple_board)
        game2 = Flow(self.simple_board)
        self.assertTrue(game1 == game2)
        changed_board = copy.deepcopy(self.simple_board)
        changed_board[1][0] = 'r'
        game2 = Flow(changed_board)
        self.assertFalse(game1 == game2)



class TestPath(TestCase):
    def setUp(self):
        simple_board = [['R', 'O', '0'],
                             ['0', '0', '0'],
                             ['R', '0', 'O']]
        self.simple_board = Flow(simple_board)

    def test_can_be_added_to_path(self):
        red_path = self.simple_board.paths['R']
        orange_path = self.simple_board.paths['O']

        self.assertTrue(red_path.can_be_added_to_path((1, 0), 0), "Point between two paths")
        self.assertTrue(orange_path.can_be_added_to_path((1, 2), 2), "Point adj to path 2 but not path 1")
        self.assertTrue(orange_path.can_be_added_to_path((0, 2), 1)), "Point adj to path 1 but not path 2"
        self.assertTrue(orange_path.can_be_added_to_path((1, 1,), 0),
                        "Point adjacent to one path, sees if either can reach it")

        self.assertFalse(orange_path.can_be_added_to_path((1, 2), 1), "Point reachable by path 2 but not path 1")
        self.assertFalse(orange_path.can_be_added_to_path((0, 2), 2), "Point reachable by path 1 but not path 2")
        self.assertFalse(red_path.can_be_added_to_path((1, 1), 0), "Point not reachable by either path")

    def test_is_complete(self):
        red_path = self.simple_board.paths['R']
        self.assertFalse(red_path.is_complete())

        red_path.path_from1.append((1, 0))
        self.assertTrue(red_path.is_complete(), "Complete because path1 ends adjacent to path2")

        red_path.path_from2.append((1, 0))
        self.assertTrue(red_path.is_complete(), "Complete because path1 and path 2 end in same spot")

    def test_add_to_path(self):
        red_path = self.simple_board.paths['R']
        red_path.add_to_path((1, 0), 0)
        self.assertTrue(red_path.path_from1[-1] == (1, 0), "Both paths contain newly added")

        orange_path = self.simple_board.paths['O']
        orange_path.add_to_path((2, 1), 2)
        self.assertTrue(orange_path.path_from2[-1] == (2, 1), "Add to second path with effect")
        self.assertFalse(orange_path.path_from1[-1] == (2, 1), "Add to first path with no effect")





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlow)
    unittest.TextTestRunner(verbosity=2).run(suite)
