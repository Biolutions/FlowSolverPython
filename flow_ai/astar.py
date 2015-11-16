from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
from copy import deepcopy
from collections import deque
import Queue as Q
import time
import sys


class astar:
    """
    :type queue: Q.PriorityQueue()
    """

    def __init__(self):
        self.queue = Q.PriorityQueue()

    def heuristic(self, game):
        F = Flow(game.board)
        """
        Gives a cost to the board state by measuring how far between growth points
        this also makes the cost max value when one path can't be moved
        :type game: Flow
        :return: double
        """
        cost = len(game.paths) * 2
        for color in game.paths:
            path = game.paths[color]
            if path.is_complete():
                cost -= 2
                continue
            gp1, gp2 = path.get_grow_points()
            # print abs((gp1[0] - gp2[0]) + (gp1[1] - gp2[1])), gp1, gp2
            cost += abs((gp1[0] - gp2[0]) + (gp1[1] - gp2[1]))
            adjecent_points = utils.get_adjacent_points(gp1)
            if not F.is_valid(adjecent_points[0][0], adjecent_points[0][1]):
                if not F.is_valid(adjecent_points[1][0], adjecent_points[1][1]):
                    if not F.is_valid(adjecent_points[2][0], adjecent_points[2][1]):
                        if not F.is_valid(adjecent_points[3][0], adjecent_points[3][1]):
                            cost = sys.maxint
                            return cost
        # print game.board[1][1]
        # for i, value in enumerate(game.board):
        #     for j in enumerate(game.board[i]):
        #         if j[1] == '0':
        #             cost += 1
        return cost

    def solve(self, initial_game_state):
        """
        :type initial_game_state: Flow
        :return Flow:
        """

        self.queue.put((astar().heuristic(initial_game_state), initial_game_state))
        current_cost = 0
        while self.queue._qsize() > 0:
            pop = self.queue.get()
            game = pop[1]
            current_cost += pop[0]
            # print current_cost
            if utils.at_goal(game):
                return game
            possible_moves = utils.generate_possible_moves_single_gp(game)
            for i, value in enumerate(possible_moves):
                # print possible_moves[i]
                self.queue.put((astar().heuristic(possible_moves[i]) + current_cost, possible_moves[i]))
        return None



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


if __name__ == '__main__':
    first_board = [['R', '0', 'G', '0', '0'],
                   ['0', '0', 'B', '0', '0'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', '0', '0'],
                   ['0', 'R', 'B', '0', '0']]

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]

    simple_board = [['R', 'Y', '0'],
                    ['0', '0', '0'],
                    ['R', '0', 'Y']]

    first_flow = Flow(first_board)
    # first_flow = Flow(simple_board)
    # first_flow = Flow(medium_flow)
    start_time = time.time()
    solution = astar().solve(first_flow)
    end_time = time.time()
    print solution
    print "Time:", end_time - start_time
    # print astar().heuristic(first_flow)