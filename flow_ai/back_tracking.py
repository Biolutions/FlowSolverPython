from flow_game.flow_board import Flow
import flow_game.utilities as utils
import copy


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
        if utils.at_goal(flow_game):
            return True, flow_game

        possible_states = utils.generate_possible_moves_single_gp(flow_game)
        for state in possible_states:
            print state
            rv = self.solve_game_dumb(copy.deepcopy(state))
            if rv[0]:
                return rv
        return False, None

    def solve_game_color(self, flow_game):
        """
        Solves the given flow game by completing one path at a time and back tracking.
        :type flow_game: Flow
        :rtype: (bool, Flow)
        """
        for color in flow_game.paths:
            path = flow_game[color]
            if not path.is_complete():
                gp1, gp2 = path.get_grow_points()
                adj_points = utils.get_adjacent_points(gp1)
                for point in adj_points:
                    if path.can_be_added_to_path(gp1, 1):
                        copy_game = copy.deepcopy(flow_game)
                        """:type:Flow"""
                        self.solve(copy_game.paths[color].add_to_path(point, 1))



if __name__ == '__main__':
    # simple_board = [['R', 'Y', '0'],
    #                 ['0', '0', '0'],
    #                 ['R', '0', 'Y']]
    #
    # simple_flow = Flow(simple_board)
    # print BackTrackSolver().solve(simple_flow)

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]
    medium_flow = Flow(medium_flow)
    print BackTrackSolver().solve(medium_flow)
    #
    # first_board = [['R', '0', 'G', '0', 'Y'],
    #                ['0', '0', 'B', '0', 'M'],
    #                ['0', '0', '0', '0', '0'],
    #                ['0', 'G', '0', 'Y', '0'],
    #                ['0', 'R', 'B', 'M', '0']]
    # first_flow = Flow(first_board)
    # print BackTrackSolver().solve(first_flow)
    #
    # hard_board =[['0', '0', '0', '0', '0', '0', 'B'],
    #              ['0', '0', '0', '0', '0', 'M', 'R'],
    #              ['0', 'M', '0', '0', '0', '0', '0'],
    #              ['0', '0', '0', 'G', 'T', '0', '0'],
    #              ['0', '0', 'G', '0', 'Y', '0', '0'],
    #              ['0', '0', '0', '0', 'R', 'Y', '0'],
    #              ['0', '0', '0', '0', '0', 'B', 'T']]
    # print BackTrackSolver().solve(Flow(hard_board))

