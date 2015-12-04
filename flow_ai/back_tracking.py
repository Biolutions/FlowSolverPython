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
            btPath = BackTrackingPath(color_path)
            completed_path = btPath.generate_new_path()
            while completed_path is not None:
                game_copy = copy.deepcopy(completed_path.flow_game)
                print game_copy
                rv = self.solve_game_dumb(game_copy)
                if rv[0]:
                    return rv
                completed_path = btPath.generate_new_path()
            return False, None

        #     gp1, gp2 = color_path.get_grow_points()
        #     adj_points = utils.get_adjacent_points(gp1)
        #     path_updated = False
        #     for possible_point in adj_points:
        #         if color_path.can_be_added_to_path(possible_point, 1):
        #             path_updated = True
        #             game_copy = copy.deepcopy(flow_game)
        #             """:type: Flow"""
        #             game_copy.paths[color].add_to_path(possible_point, 1)
        #             rv = self.solve_game_dumb(game_copy)
        #             if rv[0]:
        #                 return rv
        #     # color could not be updated
        #     if not path_updated:
        #         return False, None
        # return False, None

    # possible_states = utils.generate_possible_moves_single_gp(flow_game)
    # while len(possible_states) > 0:
    #     state = possible_states.pop(0)
    #     rv = self.solve_game_dumb(copy.deepcopy(state))
    #     if rv[0]:
    #         return rv
    # return False, None

class BackTrackingPath:
    """
    :type flow_path: Path

    """

    def __init__(self, flow_path):
        """
        :type flow_path: Path
        """
        self.flow_path = flow_path
        self.first_path_used = True
        if not flow_path.is_complete():
            self.flow_path = self.finish_path(self.flow_path)[1]
            self.first_path_used = False

        if self.flow_path is not None:
            self.restart_position = len(self.flow_path.path_from1)
            self.restart_points = []
        else:
            self.first_path_used = False

    def generate_new_path(self):
        if not self.first_path_used:
            self.first_path_used = True
            return self.flow_path

        # print len(self.flow_path.path_from1), self.restart_position, self.restart_points
        while self.restart_position > 1:

            if len(self.restart_points) == 0:
                self.restart_position -= 1
                self.restart_points.append(self.flow_path.remove_last_point(1))

            # print self.restart_points, self.restart_position
            gp1, gp2 = self.flow_path.get_grow_points()
            adj_points = utils.get_adjacent_points(gp1)
            for point in adj_points:
                if point in self.restart_points:
                    continue
                elif self.flow_path.can_be_added_to_path(point, 1):
                    self.restart_points.append(point)
                    copy_path = copy.deepcopy(self.flow_path)
                    """:type: Path"""
                    copy_path.add_to_path(point, 1)
                    rv = self.finish_path(copy_path)
                    if rv[0]:
                        # print "RETURNING"
                        return rv[1]
            self.restart_points = []




    def finish_path(self, path):
        """
        :type path: Path
        :return:
        """
        if path.is_complete():
            # print path.flow_game
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
    # simple_board = [['R', 'Y', '0'],
    #                 ['0', '0', '0'],
    #                 ['R', '0', 'Y']]
    #
    # simple_flow = Flow(simple_board)
    # start = time.time()
    # print BackTrackSolver().solve(simple_flow)
    # print "Back Track simple:", str(time.time() - start)

    # medium_flow = [['R', 'Y', '0'],
    #                ['0', '0', '0'],
    #                ['G', '0', '0'],
    #                ['0', 'R', '0'],
    #                ['0', 'G', 'Y']]
    # medium_flow = Flow(medium_flow)


    start = time.time()
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

    hard = Flow(hard_board)
    bt = BackTrackingPath(hard.paths['B'])
    rv = bt.generate_new_path()
    while (rv is not None):
        print rv.flow_game
        rv = bt.generate_new_path()

    # start = time.time()
    # print BackTrackSolver().solve(Flow(hard_board))
    # print "Back Track hard:", str(time.time() - start)



