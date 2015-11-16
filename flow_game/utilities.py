from flow_board import Flow
import copy


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
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]


def generate_possible_moves_single_gp(game):
    """
    Takes in a game and updates the queue. New game states are added as if only 1 growth point for each color is
    allowed to make a move.
    :type game: Flow
    :rtype: list[Flow]
    """
    found_games = []
    for color in game.paths:
        path = game.paths[color]
        if path.is_complete():
            continue
        gp1, gp2 = path.get_grow_points()
        adj2gp1 = get_adjacent_points(gp1)
        for possible in adj2gp1:
            if path.can_be_added_to_path(possible, 1):
                copy_game = copy.deepcopy(game)
                """:type: Flow"""
                copy_game.paths[color].add_to_path(possible, 1)
                if is_unique(found_games, copy_game):
                    found_games.append(copy_game)
    return found_games


def generate_possible_moves_rr(game):
    """
    THIS FUNCTION DOES NOT CHECK FOR UNIQUE GAMES

    Takes in a game and updates the queue. Games are added as if each grow point got a turn to pick a space.
    Colors will alternate.

    :type game: Flow
    :rtype: list[Flow]
    """
    found_games = []
    gp1_games = []
    gp2_games = []
    for color in game.paths:
        # TODO clean up expression
        path = game.paths[color]

        # Get grow points and points adjacent to them
        gp1, gp2 = path.get_grow_points()
        adj2gp1 = get_adjacent_points(gp1)
        adj2gp2 = get_adjacent_points(gp2)

        # Handle adding adjacent points to grow points separately - in order to maintain RR order.
        for possible in adj2gp1:
            if path.can_be_added_to_path(possible, 1):
                copy_game = copy.deepcopy(game)
                """:type: Flow"""
                copy_game.paths[color].add_to_path(possible, 1)
                gp1_games.append(copy_game)

        for possible in adj2gp2:
            if path.can_be_added_to_path(possible, 1):
                copy_game = copy.deepcopy(game)
                """:type: Flow"""
                copy_game.paths[color].add_to_path(possible, 2)
                gp2_games.append(copy_game)

    # Add games to queue
    return found_games.append(gp1_games + gp2_games)


def is_unique(flow_list, flow_game):
    """
    Makes sure that the flow_game is not already contained in the given list.

    :type flow_list: list[Flow]
    :type flow_game: Flow
    :rtype: bool
    """

    for known_game in flow_list:
        if known_game == flow_game:
            return False
    return True


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

