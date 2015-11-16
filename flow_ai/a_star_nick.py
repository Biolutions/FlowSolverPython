from flow_game.flow_board import Flow
from a_star_skeleton import AbstractAStar


class AStarNick(AbstractAStar):

    def heuristic(self, flow_game):
        """
        Overrides the heuristic method of AbstractAStar
        :type flow_game: Flow
        :rtype: int
        """
        hcost = 0
        # Iterate over the paths. Count the cost to complete each path
        # TODO Write more pythonic
        for path in flow_game.paths.values():
            if not path.is_complete():
                gp1, gp2 = path.get_grow_points()
                row1, col1 = gp1[0], gp1[1]
                row2, col2 = gp2[0], gp2[1]
                hcost += abs(row1 - row2) + abs(row2 + col2) - 1
        return hcost

if __name__ == '__main__':
    # simple_board = [['R', 'Y', '0'],
    #             ['0', '0', '0'],
    #             ['R', '0', 'Y']]
    #
    # simple_flow = Flow(simple_board)
    # print AStarNick().solve(simple_flow)[1]

    medium_flow = [['R', 'Y', '0'],
                   ['0', '0', '0'],
                   ['G', '0', '0'],
                   ['0', 'R', '0'],
                   ['0', 'G', 'Y']]
    medium_flow = Flow(medium_flow)
    print AStarNick().solve(medium_flow)[1]
    #
    # first_board = [['R', '0', 'G', '0', 'Y'],
    #                ['0', '0', 'B', '0', 'M'],
    #                ['0', '0', '0', '0', '0'],
    #                ['0', 'G', '0', 'Y', '0'],
    #                ['0', 'R', 'B', 'M', '0']]
    # first_flow = Flow(first_board)
    # print AStarNick().solve(first_flow)[1]