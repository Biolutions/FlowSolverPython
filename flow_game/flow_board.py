from copy import deepcopy


class Flow:
    """
    Object that models the game "Flow" Contains methods needed for determining if points exist in the board. And
    modifying/ storing paths on the board.

    :type paths: dict[str, Path]
    :type board: list[list[str]]
    """
    paths = {}
    board = []

    def __init__(self, board):
        """
        :type board: list [list[str]]
        """
        self.board = board
        self.paths = {}
        self.find_end_points()

    def __eq__(self, other):
        if not isinstance(other, Flow):
            raise ValueError("Argument was not Flow object! Cannot compare to another Flow!")
        board1 = self.board
        board2 = other.board
        if len(board1) != len(board2) or len(board1[0]) != len(board2[0]):
            return False
        for row in range(0, len(board1)):
            for col in range(0, len(board2[row])):
                if board1[row][col] != board2[row][col]:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def find_end_points(self):
        """
        Looks at the board attribute to find all of the end points that are in the game. End points are any all upper
        case value.
        :return: None
        """
        end_points_finder = {}
        for row in range(0, len(self.board)):

            for col in range(0, len(self.board[row])):
                value = self.board[row][col]

                # If the value is upper case and already in the dictionary. Append it's coordinate
                if value.isupper() and value in end_points_finder:
                    end_points_finder[value].append((row, col))

                # If the value is upper case and not already in the dictionary.
                # Add it with a new list containing the coordinate
                elif value.isupper() and value not in end_points_finder:
                    end_points_finder[value] = [(row, col)]

        # Use the gather information to create Path Classes
        for color in end_points_finder:
            end_point1 = end_points_finder[color][0]
            end_point2 = end_points_finder[color][1]
            self.paths[color] = Path(color, end_point1, end_point2, self)

    def get_board_copy(self):
        return deepcopy(self.board)

    def is_valid(self, row, col):
        """
        Determines row, col exist in the board
        :type col: int
        :type row: int
        :rtype: bool
        """
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):
            return False
        return True

    def is_empty(self, row, col):
        """
        Determines if the position at row, col is empty.
        :type row: int
        :type col: int
        :rtype: bool
        """

        if self.is_valid(row, col) and self.board[row][col] == '0':
            return True

        return False

    def adjacent_points(self, point1, point2):
        """
        Determines if 2 points are adjacent to one another in the given board.
        Returns false if either point is invalid.
        :rtype: bool
        """
        row1 = point1[0]
        col1 = point1[1]
        row2 = point2[0]
        col2 = point2[1]
        if not self.is_valid(row1, col1) or not self.is_valid(row2, col2):
            return False
        if (abs(row1 - row2) + abs(col1 - col2)) == 1:
            return True
        return False

    def __str__(self):
        ret_str = "Board \n"
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                ret_str += self.board[row][col].rjust(3, ' ')
            ret_str += '\n'
        return ret_str

    def get_unfinished_paths(self):
        unfinished = []
        for path in self.paths.values():
            if not path.is_complete():
                unfinished.append(path)
        return unfinished

class Path:
    """
    :type path_from1: list[(int, int)]
    :type path_from2: list[(int, int)]
    :type color: str
    :type flow_game: Flow
    """
    path_from1 = []
    path_from2 = []
    color = ""

    def __init__(self, color, end_point1, end_point2, flow_game):
        """
        :type color: str
        :type end_point1: (int, int)
        :type end_point2: (int, int)
        :type flow_game: Flow
        :type: None
        """
        self.color = color
        self.path_from1 = [end_point1]
        self.path_from2 = [end_point2]
        self.flow_game = flow_game

    def is_complete(self):
        """
        Determines if the path is complete by comparing the last element in the two path lists.
        If they are the same or adjacent to one another then the path is complete.
        :rtype: bool
        """
        route1_end = self.path_from1[-1]
        route2_end = self.path_from2[-1]
        if route1_end == route2_end:
            return True

        if self.flow_game.adjacent_points(route1_end, route2_end):
            return True
        return False

    def get_complete_path(self):
        """
        Returns a list of tuples that represents the complete path. If the path is not complete returns "not complete".
        :rtype: list[(int, int)]
        """
        if not self.is_complete():
            return "Not complete"

        complete_path = []
        for point in self.path_from1:
            if point not in self.path_from2:
                complete_path.append(point)
        for point in self.path_from2:
            if point not in self.path_from1:
                complete_path.append(point)

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
        # TODO: write unit test
        was_added = False

        # Attempt to add to path 1
        if route_num == 0 or route_num == 1:
            if self.can_be_added_to_path(point, 1):
                self.path_from1.append(point)
                was_added = True
        # Attempt to add to path 2
        if route_num == 0 or route_num == 2:
            if self.can_be_added_to_path(point, 2):
                self.path_from2.append(point)
                was_added = True

        if was_added:
            self.flow_game.board[point[0]][point[1]] = self.color.lower()

    def get_grow_points(self):
        """
        Returns the two points that can be grown from.
        :rtype: ((int, int), (int, int))
        """
        return self.path_from1[-1], self.path_from2[-1]
