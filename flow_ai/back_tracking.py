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
        while len(possible_states) > 0:
            state = possible_states.pop(0)
            rv = self.solve_game_dumb(copy.deepcopy(state))
            if rv[0]:
                return rv
        return False, None

if __name__ == '__main__':
    simple_board = [['R', 'Y', '0'],
                    ['0', '0', '0'],
                    ['R', '0', 'Y']]

    simple_flow = Flow(simple_board)
    print BackTrackSolver().solve(simple_flow)

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]
    medium_flow = Flow(medium_flow)
    print BackTrackSolver().solve(medium_flow)

    first_board = [['R', '0', 'G', '0', 'Y'],
                   ['0', '0', 'B', '0', 'M'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', 'Y', '0'],
                   ['0', 'R', 'B', 'M', '0']]
    first_flow = Flow(first_board)
    print BackTrackSolver().solve(first_flow)


