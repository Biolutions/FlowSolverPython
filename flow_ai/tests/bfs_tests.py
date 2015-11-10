import unittest
from flow_ai.bfs import BFS
from flow_game.flow_board import Flow
import flow_game.utilities as utils

class TestBFS(unittest.TestCase):

    def setUp(self):
        self.simple_board = [['R', 'Y', '0'],
                             ['0', '0', '0'],
                             ['R', '0', 'Y']]

        self.medium_flow = [['R', 'Y', '0'],
                            ['0', '0', '0'],
                            ['G', '0', '0'],
                            ['0', 'R', '0'],
                            ['0', 'G', 'Y']]

    def test_round_robin(self):
        flow_game = Flow(self.simple_board)
        solution = BFS().solve_rr(flow_game)
        self.assertTrue(utils.at_goal(solution),
                        "Test if BFS solves the simple board with RR method of adding to queue")

        flow_game = Flow(self.medium_flow)
        solution = BFS().solve_single_gp(flow_game)
        self.assertTrue(utils.at_goal(solution),
                        "Test if BFS solves the medium board with RR method of adding to queue")

    def test_single_gp(self):
        flow_game = Flow(self.simple_board)
        solution = BFS().solve_single_gp(flow_game)
        self.assertTrue(utils.at_goal(solution),
                        "Tests if BFS solves simple board with single GP method of adding to queue")

        flow_game = Flow(self.medium_flow)
        solution = BFS().solve_single_gp(flow_game)
        self.assertTrue(utils.at_goal(solution),
                        "Tests if BFS solves medium board with single GP method of adding to queue")

if __name__ == '__main__':
    unittest.TestLoader().loadTestsFromTestCase(TestBFS).run()