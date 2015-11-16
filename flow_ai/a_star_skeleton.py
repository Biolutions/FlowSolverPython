from flow_game.flow_board import Flow
import flow_game.utilities as utils

class AbstractAStar:
    """
    :type frontier: list[(int, Flow)]
    """
    def __init__(self):
        self.frontier = []

    def solve(self, initial_flow):
        """
        Solve the initial flow game

        :type initial_flow: Flow
        :rtype: Flow
        """
        self.frontier.append((0, initial_flow))
        while len(self.frontier) > 0:
            chosen_node = self.get_next_to_explore()
            print chosen_node[0], chosen_node[1]
            if utils.at_goal(chosen_node[1]):
                return chosen_node
            else:
                self.create_possibilites(chosen_node)

        return "No solution found"

    def get_next_to_explore(self):
        """
        Returns the node with the lowest value will remove it from the list

        :rtype: Flow
        """
        self.frontier.sort(key=lambda node: node[0])
        return self.frontier.pop(0)

    def create_possibilites(self, node):
        """
        Gets a list of possible new moves, makes sure they are not already in the list, applies heurstic and adds them
        :type node: (int, Flow)
        """
        new_states = utils.generate_possible_moves_single_gp(node[1])
        for new_state in new_states:
            if new_state not in [node[1] for node in self.frontier]:
                # New cost is the cost of the heuristic, plus the cost of the parent node, plus 1.
                cost = self.heuristic(new_state) + node[0] + 1
                self.frontier.append((cost, new_state))

    def heuristic(self, flow_game):
        abstract


