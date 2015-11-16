from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
from copy import deepcopy
from collections import deque
import Queue as Q
import time


class astar:
    """
    :type queue: Q.PriorityQueue()
    """

    def __init__(self):
        self.queue = Q.PriorityQueue()

    def heuristic(self, game):
        """
        :type game: Flow
        :return: double
        """
        cost = len(game.paths) * 2
        for color in game.paths:
            path = game.paths[color]
            if path.is_complete():
                cost -= 1
        # print game.board[1][1]
        for i, value in enumerate(game.board):
            for j in enumerate(game.board[i]):
                if j[1] == '0':
                    cost += 1
        return cost

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
            # if path.is_complete():=
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
                    temp = Flow(copy_game)
                    self.queue.put((astar.heuristic(temp), copy_game))

        # Add games to queue

        # self.queue.put((astar.heuristic(gp1_games), gp1_games))
        # self.queuue.put((astar.heuristic(gp1_games), gp1_games))
        # self.queue.put((astar.heuristic(gp2_games), gp2_games))

    # def solve(self, initial_game_state):
    #     """
    #     :type initial_game_state: Flow
    #     :return Flow:
    #     """
    #
    #     self.queu.append(initial_game_state)

    def can_be_added_to_path(self, point, route_num=0):
        """
        Determines if a point is adjacent to the last point in the specified path.
        Path 0 is both paths, path 1 for end point 1, path 2 for end point 2.
        If no path is specified it sees if the point can be added to either path.
        If the path is already complete (connected) then it return false

        :type point: (int, int)
        :type route_num: int
        :rtype: bool
        """

        if self.is_complete():
            return False
        # TODO: Write unit test
        if not self.flow_game.is_empty(point[0], point[1]):
            return False
        available_end1 = self.path_from1[-1]
        available_end2 = self.path_from2[-1]
        can_be_added = False

        # Check the first path
        if route_num == 0 or route_num == 1:
            can_be_added = self.flow_game.adjacent_points(available_end1, point)
        if route_num == 0 or route_num == 2:
            can_be_added = can_be_added or self.flow_game.adjacent_points(available_end2, point)

        return can_be_added

    def add_to_path(self, point, route_num=0):
        """
        Adds the point to the specified route.

        :param route_num: 0, add to both / either path. 1 add to path 1, 2 add to path 2
        """
        current_queue = list()

        # TODO: write unit test
        was_added = False

        # Attempt to add to path 1
        if route_num == 0 or route_num == 1:
            if self.can_be_added_to_path(point, 1):
                self.path_from1.append(point)
                current_queue.append()
                was_added = True
        # Attempt to add to path 2
        if route_num == 0 or route_num == 2:
            if self.can_be_added_to_path(point, 2):
                self.path_from2.append(point)
                was_added = True

        if was_added:
            self.flow_game.board[point[0]][point[1]] = self.color.lower()

    def solve_rr(self, initial_game_state):
        """
        Creates the stack to be searched in a round robin manner - Each color gets to select 1 move until the solution
        is found.
        :type initial_game_state: Flow
        :return: Flow
        """
        self.queue.put((astar().heuristic(initial_game_state), initial_game_state))
        # print self.queue.get()

        # For loop to go through queue
        while self.queue.qsize() > 0:
            pop = tuple()
            pop = self.queue.get()
            game = pop[1]
            print 1
            if utils.at_goal(game):
                return game
            self.generate_possible_moves_rr(game)
        return None

if __name__ == '__main__':
    first_board = [['R', '0', 'G', '0', '0'],
                   ['0', '0', 'B', '0', '0'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', '0', '0'],
                   ['0', 'R', 'B', '0', '0']]

    first_flow = Flow(first_board)
    start_time = time.time()
    solution = astar().solve_rr(first_flow)
    end_time = time.time()
    print solution
    print "Time:", end_time - start_time
    # print astar().heuristic(first_flow)