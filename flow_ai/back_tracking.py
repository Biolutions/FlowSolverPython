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

        sorted_colors = self.order_colors(flow_game)
        # For each color that is not complete
        for color_path in sorted_colors:
            if color_path.is_complete():
                continue
            # Complete its path
            bt_path = BackTrackingPath(color_path)
            completed_path = bt_path.get_next_path()
            # While there are still backtracking options
            while completed_path is not None:
                game_copy = copy.deepcopy(completed_path.flow_game)
                rv = self.solve_game_dumb(game_copy)
                if rv[0]:
                    return rv
                completed_path = bt_path.get_next_path()
            return False, None

    def order_colors(self, flow_game):
        """
        :type flow_game: Flow
        :return: Path
        """
        distances = []
        for color in flow_game.paths:
            path = flow_game.paths[color]
            if path.is_complete():
                continue
            else:
                sp1 = path.path_from1[0]
                sp2 = path.path_from2[0]
                distances.append((abs(sp1[0] - sp2[0]) + abs(sp1[1] - sp2[0]), path))
        distances.sort(key=lambda x: x[0])
        return [y[1] for y in distances]

class BackTrackingPath:
    """
    :type flow_path: Path
    :type paths_queue: list[Path]
    :type last_restart: Path

    """

    def __init__(self, flow_path):
        """
        :type flow_path: Path
        """
        if not flow_path.is_complete():
            flow_path = self.finish_path(flow_path)[1]

        self.last_restart = copy.deepcopy(flow_path)
        self.paths_queue = [flow_path]

    def get_next_path(self):
        if len(self.paths_queue) > 0:
            return self.paths_queue.pop(0)
        else:
            # While the last restart has more than just the origin
            while len(self.last_restart.path_from1) > 1:
                restart_path = self.last_restart
                restart_path.remove_last_point(1)
                self.last_restart = copy.deepcopy(restart_path)
                # print "Restart path", len(restart_path.path_from1), restart_path.flow_game
                self.generate_new_paths(restart_path)
                if len(self.paths_queue) > 0:
                    self.paths_queue.sort(key=lambda path: len(path.path_from1))
                    return self.paths_queue.pop(0)
            return None

    def generate_new_paths(self, path):
        """

        :type path: Path
        :return: None
        """
        if path.is_complete():
            self.paths_queue.append(path)
            # print "Adding path, num paths", len(self.paths_queue), path.flow_game

        gp1, gp2 = path.get_grow_points()
        adj_points = utils.get_adjacent_points(gp1)
        for point in adj_points:
            if path.can_be_added_to_path(point):
                copy_path = copy.deepcopy(path)
                """:type:Path"""
                copy_path.add_to_path(point)
                self.generate_new_paths(copy_path)

    def finish_path(self, path):
        """
        :type path: Path
        :type add_to_queue: bool
        :return:
        """

        if path.is_complete():
            return True, path

        gp1, gp2 = path.get_grow_points()
        adj_points = utils.get_adjacent_points(gp1)
        for point in adj_points:
            if path.can_be_added_to_path(point):
                copy_path = copy.deepcopy(path)
                """:type:Path"""
                copy_path.add_to_path(point)
                rv = self.finish_path(copy_path)
                if rv[0]:
                    return rv
        return False, None

if __name__ == '__main__':
    simple_board = [['R', 'Y', '0'],
                    ['0', '0', '0'],
                    ['R', '0', 'Y']]

    simple_flow = Flow(simple_board)
    start = time.time()
    print BackTrackSolver().solve(simple_flow)
    print "Back Track simple:", str(time.time() - start)

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]
    medium_flow = Flow(medium_flow)


    start = time.time()
    print BackTrackSolver().solve(medium_flow)
    print "Back Track medium:", str(time.time() - start)


    first_board = [['R', '0', 'G', '0', 'Y'],
                   ['0', '0', 'B', '0', 'M'],
                   ['0', '0', '0', '0', '0'],
                   ['0', 'G', '0', 'Y', '0'],
                   ['0', 'R', 'B', 'M', '0']]
    first_flow = Flow(first_board)
    start = time.time()
    print BackTrackSolver().solve(first_flow)
    print "Back Track first:", str(time.time() - start)


    hard_board =[['0', '0', '0', '0', '0', '0', 'B'],
                 ['0', '0', '0', '0', '0', 'M', 'R'],
                 ['0', 'M', '0', '0', '0', '0', '0'],
                 ['0', '0', '0', 'G', 'T', '0', '0'],
                 ['0', '0', 'G', '0', 'Y', '0', '0'],
                 ['0', '0', '0', '0', 'R', 'Y', '0'],
                 ['0', '0', '0', '0', '0', 'B', 'T']]

    # hard = Flow(hard_board)
    # bt = BackTrackingPath(hard.paths['B'])
    # rv = bt.get_next_path()
    # while (rv is not None):
    #     # print rv.flow_game
    #     rv = bt.get_next_path()

    start = time.time()
    print BackTrackSolver().solve(Flow(hard_board))
    print "Back Track hard:", str(time.time() - start)



