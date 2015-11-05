from copy import deepcopy


class Flow:

    def __init__(self, board):
        """
        :type board: list [list[str]]
        """

        self._board = board

    def get_board_copy(self):
        return deepcopy(self._board)

    def __str__(self):
        ret_str = ""
        for row in range(0, len(self._board)):
            for col in range(0, len(self._board[row])):
                ret_str += self._board[row][col].rjust(3, ' ')
            ret_str += '\n'
        return ret_str
