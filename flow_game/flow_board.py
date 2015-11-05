from copy import deepcopy


class Flow:
    """
    :type _end_points: dict[str, list[(int, int)]]
    :type board: list[list[str]]
    """
    _end_points = {}

    def __init__(self, board):
        """
        :type board: list [list[str]]
        """
        self.board = board
        self.find_end_points()

    def find_end_points(self):
        """
        Looks at the _board attribute to find all of the end points that are in the game. End points are any all upper
        case value.
        :return: None
        """
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                value = self.board[row][col]

                # If the value is upper case and already in the dictionary. Append it's coordinate
                if value.isupper() and value in self._end_points:
                    self._end_points[value].append((row, col))

                # If the value is upper case and not already in the dictionary.
                # Add it with a new list containing the coordinate
                elif value.isupper() and value not in self._end_points:
                    self._end_points[value] = [(row, col)]

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


    def __str__(self):
        ret_str = "Board \n"
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                ret_str += self.board[row][col].rjust(3, ' ')
            ret_str += '\n'
        return ret_str
