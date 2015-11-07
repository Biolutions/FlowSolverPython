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

def get_adjacent_points(point):
    """
    Returns a list of the 4 points that are adjacent to the given point. These points may or may not exist on board.

    :type point: (int, int)
    :return: list[(int, int)]
    """
    row = point[0]
    col = point[1]
    return [(row +1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def at_goal(board):
    """
    Determines if the board is in the goal state.

    :type board: Flow
    :rtype: bool
    """
    done = True
    for path in board.paths.values():
        done = done and path.is_complete()
    return done

