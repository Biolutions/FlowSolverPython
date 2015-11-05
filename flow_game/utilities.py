from flow_board import Flow


def load_game(filename):
    """
    Takes a file and returns a new flowBoard object
    :type filename: str
    :rtype: Flow
    """

    board = []
    input_file = open(filename, 'r')
    for line in input_file:
        row = [x.strip() for x in line.split(',')]
        board.append(row)

    return Flow(board)

def equal_boards(board1, board2):
    """
    Checks to see if 2 boards are equal.
    
    :type board1: list[list[str]]
    :type board2: list[list[str]]
    :rtype: bool
    """
    if len(board1) != len(board2) or len(board1[0]) != len(board2[0]):
        return False

    for row in range(0, len(board1)):
        for col in range(0, len(board2)):
            if board1[row][col] != board2[row][col]:
                return False
    return True

def convert_to_xy(board):
    """
    Takes in a board that is in the form [row][col] ([y][x]) and converts it to the form
    [x][y] or [col][row]
    :param board:
    :return:
    """
    xy_board = []
    for y in range(0, len(board)):
        x_vals = []
        for x in range(0, len(board[y])):
            x_vals.append(board[x][y])
        xy_board.append(x_vals)
    return xy_board

