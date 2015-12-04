from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
import copy, time


class BackTrackSolver:

    def solve_file(self, filename):
        """
        Solves the board in filename
        :type filename: str
        :rtype: Flow
        """

    def solve(self, initial_game):
        """

        :type initial_game: Flow
        :rtype: Flow
        """
        rv = self.solve_game_dumb(initial_game)
        if rv[0]:
            return rv[1]
        else:
            return "No solution"

    def solve_game_dumb(self, flow_game):
        """
        Solves the given flow game using backtracking.
        :type flow_game: Flow
        :rtype: (bool, Flow)
        """
        # print flow_game
        if utils.at_goal(flow_game):
            return True, flow_game

        for color in flow_game.paths:
            color_path = flow_game.paths[color]
            if color_path.is_complete():
                continue

            gp1, gp2 = color_path.get_grow_points()
            adj_points = utils.get_adjacent_points(gp1)
            path_updated = False
            for possible_point in adj_points:
                if color_path.can_be_added_to_path(possible_point, 1):
                    path_updated = True
                    game_copy = copy.deepcopy(flow_game)
                    """:type: Flow"""
                    game_copy.paths[color].add_to_path(possible_point, 1)
                    rv = self.solve_game_dumb(game_copy)
                    if rv[0]:
                        return rv
            # color could not be updated
            if not path_updated:
                return False, None
        return False, None

    # possible_states = utils.generate_possible_moves_single_gp(flow_game)
    # while len(possible_states) > 0:
    #     state = possible_states.pop(0)
    #     rv = self.solve_game_dumb(copy.deepcopy(state))
    #     if rv[0]:
    #         return rv
    # return False, None

class backTrackingPath:

    def __init__(self, flow_path):
        """
        :type flow_path: Path
        """
        self.flow_path = flow_path
        self.restart_points = []


    def generate_path(self):
        """
        :return:
        """

    def finish_path(self, propsed_path):
        """
        :type

        :return:
        """


if __name__ == '__main__':
    # simple_board = [['R', 'Y', '0'],
    #                 ['0', '0', '0'],
    #                 ['R', '0', 'Y']]
    #
    # simple_flow = Flow(simple_board)
    # start = time.time()
    # print BackTrackSolver().solve(simple_flow)
    # print "Back Track simple:", str(time.time() - start)
    #
    # medium_flow = [['R', 'Y', '0'],
    #                ['0', '0', '0'],
    #                ['G', '0', '0'],
    #                ['0', 'R', '0'],
    #                ['0', 'G', 'Y']]
    # medium_flow = Flow(medium_flow)
    # start = time.time()
    # print BackTrackSolver().solve(medium_flow)
    # print "Back Track medium:", str(time.time() - start)
    #
    #
    # first_board = [['R', '0', 'G', '0', 'Y'],
    #                ['0', '0', 'B', '0', 'M'],
    #                ['0', '0', '0', '0', '0'],
    #                ['0', 'G', '0', 'Y', '0'],
    #                ['0', 'R', 'B', 'M', '0']]
    # first_flow = Flow(first_board)
    # start = time.time()
    # print BackTrackSolver().solve(first_flow)
    # print "Back Track first:", str(time.time() - start)


    hard_board =[['0', '0', '0', '0', '0', '0', 'B'],
                 ['0', '0', '0', '0', '0', 'M', 'R'],
                 ['0', 'M', '0', '0', '0', '0', '0'],
                 ['0', '0', '0', 'G', 'T', '0', '0'],
                 ['0', '0', 'G', '0', 'Y', '0', '0'],
                 ['0', '0', '0', '0', 'R', 'Y', '0'],
                 ['0', '0', '0', '0', '0', 'B', 'T']]
    start = time.time()
    print BackTrackSolver().solve(Flow(hard_board))
    print "Back Track hard:", str(time.time() - start)



