from flow_game.flow_board import Flow, Path
import flow_game.utilities as utils
from collections import deque


class BFS:
    """
    :type queue: deque([Flow])
    """

    def __init__(self):
        self.queue = deque([])

    def solve(self, filename):
        start = utils.load_game(filename)

    def round_robin_solve(self, initial_game_state, colors):
        """
        Creates the stack to be searched in a round robin manner - Each color gets to select 1 move until the solution
        is found.
        :type initial_game_state: Flow
        :type colors: list[Path]
        :return: Flow
        """
        self.queue.append(initial_game_state)

        for game in self.queue:
            grow_points1 = game.










if __name__ == '__main__':
    print "bfs"
