from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
from copy import deepcopy
import time


class BFS:
    """
    :type queue: List[Flow]
    """

    def __init__(self):
        self.queue = []

    def solve_file(self, filename, method="RR"):
        start = utils.load_game(filename)
        if method.lower() == "RR":
            return self.solve_rr(start)
        else:
            return self.solve_single_gp(start)

    def solve_rr(self, initial_game_state):
        """
        Creates the stack to be searched in a round robin manner - Each color gets to select 1 move until the solution
        is found.
        :type initial_game_state: Flow
        :return: Flow
        """
        self.queue.append(initial_game_state)

        # For loop to go through queue
        while len(self.queue) > 0:
            game = self.queue.pop(0)
            if utils.at_goal(game):
                return game
            self.generate_possible_moves_rr(game)
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
            # if path.is_complete():
            #     continue

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

    def solve_single_gp(self, initial_game):
        """
        Creates the stack to be searched in a round robin manner - Each color gets to select 1 move until the solution
        is found.
        :type initial_game_state: Flow
        :return: Flow
        """
        self.queue.append(initial_game)

        # For loop to go through queue
        while len(self.queue) > 0:
            game = self.queue.pop(0)
            if utils.at_goal(game):
                return game
            self.generate_possible_moves_single_gp(game)
        return None

    def generate_possible_moves_single_gp(self, game):
        """
        Takes in a game and upates the queue. New game states are added is if only 1 growth point for each color is
        allowed to make a move.
        :type game: Flow
        """
        for color in game.paths:
            path = game.paths[color]
            if path.is_complete():
                continue
            gp1, gp2 = path.get_grow_points()
            adj2gp1 = utils.get_adjacent_points(gp1)
            for possible in adj2gp1:
                # print "Attempting"
                # print game
                # print possible, path.can_be_added_to_path(possible, 1)
                if path.can_be_added_to_path(possible, 1):
                    copy_game = deepcopy(game)
                    """:type: Flow"""
                    copy_game.paths[color].add_to_path(possible, 1)
                    self.queue.append(copy_game)
                    # print "after attempt"
                    # print copy_game

if __name__ == '__main__':
    simple_board = [['R', 'Y', '0'],
                    ['0', '0', '0'],
                    ['R', '0', 'Y']]

    simple_flow = Flow(simple_board)
    # print BFS().solve_rr(simple_flow)
    start = time.time()
    print BFS().solve_single_gp(simple_flow)
    print "Simple board time:", str(time.time() - start)

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]
    medium_flow = Flow(medium_flow)
    # print BFS().solve_rr(medium_flow)
    start = time.time()
    print BFS().solve_single_gp(medium_flow)
    print "Medium flow time:", str(time.time() - start)

    first_board = [['R', '0', 'G', '0', '0'],
                   ['0', '0', 'B', '0', '0'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', '0', '0'],
                   ['0', 'R', 'B', '0', '0']]
    first_flow = Flow(first_board)

    start_time = time.time()
    solution = BFS().solve_rr(first_flow)
    end_time = time.time()
    print solution
    print "Time:", end_time - start_time

    start_time = time.time()
    solution2 = BFS().solve_single_gp(first_flow)
    end_time = time.time()
    print "Time:", end_time - start_time
    print solution2

