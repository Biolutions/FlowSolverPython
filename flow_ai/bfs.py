from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
from copy import deepcopy


class BFS:
    """
    :type queue: List[Flow]
    """

    def __init__(self):
        self.queue = []

    def solve(self, filename):
        start = utils.load_game(filename)
        return self.round_robin_solve(start)

    def round_robin_solve(self, initial_game_state):
        """
        Creates the stack to be searched in a round robin manner - Each color gets to select 1 move until the solution
        is found.
        :type initial_game_state: Flow
        :return: Flow
        """
        self.queue.append(initial_game_state)

        # For loop to go through queue
        for game in self.queue:
            if utils.at_goal(game):
                return game
            self.generate_possible_moves_rr(game)
            self.queue.remove(game)
        return None

    def generate_possible_moves_rr(self, game):
        """
        Takes in a game and updates the queue. Games are added as if each grow point got a turn to pick a space.
        Colors will alternate.

        :type game: Flow
        """
        gp1_games = []
        gp2_games = []
        for color in game.paths:
            # TODO clean up expression
            path = game.paths[color]
            if path.is_complete():
                continue

            # Get grow points and points adjacent to them
            gp1, gp2 = path.get_grow_points()
            adj2gp1 = utils.get_adjacent_points(gp1)
            adj2gp2 = utils.get_adjacent_points(gp2)

            # Handle adding adjacent points to grow points separately - in order to maintain RR order.
            for possible in adj2gp1:
                if path.can_be_added_to_path(possible, 1):
                    copy_game = deepcopy(game)
                    """:type: Flow"""
                    copy_game.paths[color].add_to_path(possible, 1)
                    gp1_games.append(copy_game)

            for possible in adj2gp2:
                if path.can_be_added_to_path(possible, 1):
                    copy_game = deepcopy(game)
                    """:type: Flow"""
                    copy_game.paths[color].add_to_path(possible, 2)
                    gp2_games.append(copy_game)

        # Add games to queue
        self.queue += gp1_games + gp2_games


if __name__ == '__main__':
    # simple_board = [['R', 'Y', '0'],
    #                 ['0', '0', '0'],
    #                 ['R', '0', 'Y']]
    #
    # simple_flow = Flow(simple_board)
    # print BFS().round_robin_solve(simple_flow)
    #
    # medium_flow = [['R', 'Y', '0'],
    #                ['0', '0', '0'],
    #                ['G', '0', '0'],
    #                ['0', 'R', '0'],
    #                ['0', 'G', 'Y']]
    # medium_flow = Flow(medium_flow)
    # print BFS().round_robin_solve(medium_flow)

    first_board = [['R', '0', 'G', '0', '0'],
                   ['0', '0', 'B', '0', '0'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', '0', '0'],
                   ['0', 'R', 'B', '0', '0']]
    first_flow = Flow(first_board)
    solution = BFS().round_robin_solve(first_flow)
    print solution
    print utils.at_goal(solution)
    for path in solution.paths.values():
        """:type:Flow """
        print path.get_complete_path(), path.is_complete()
        print path.color, path.path_from1, path.path_from2

