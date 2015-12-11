import a_star_nick as astar
import back_tracking
import bfs
import flow_game.utilities as utils
import time


def time_run(method, board, number_of_runs):
    total_time = 0
    for x in range(0, number_of_runs):
        startTime = time.time()
        method(board)
        total_time += (time.time() - startTime)
    return str(total_time/number_of_runs)


if __name__ == '__main__':
    PATH_TO_TEST_FILES = "../TestBoards/"
    simpleFlow = utils.load_game(PATH_TO_TEST_FILES+"simpleBoard.txt")
    mediumFlow = utils.load_game(PATH_TO_TEST_FILES+"mediumBoard.txt")
    firstFlow = utils.load_game(PATH_TO_TEST_FILES+"easy5x5.txt")
    hardFlow = utils.load_game(PATH_TO_TEST_FILES+"7x7board.txt")
    hardestFlow = utils.load_game(PATH_TO_TEST_FILES+"9x9board.txt")

    bfsAI = bfs.BFS()
    astarAI = astar.AStarNick()
    backtrackingAI = back_tracking.BackTrackSolver()

    print "3x3 2 colors"
    print "bfs:", time_run(bfsAI.solve_single_gp, simpleFlow, 100)
    print "astar:", time_run(astarAI.solve, simpleFlow, 100)
    print "backtracking:", time_run(backtrackingAI.solve, simpleFlow, 100)
    print

    bfsAI = bfs.BFS()
    astarAI = astar.AStarNick()
    backtrackingAI = back_tracking.BackTrackSolver()
    print "5x3 3 colors"
    print "bfs:", time_run(bfsAI.solve_single_gp, mediumFlow, 100)
    print "astar:", time_run(astarAI.solve, mediumFlow, 100)
    print "backtracking:", time_run(backtrackingAI.solve, mediumFlow, 100)
    print

    bfsAI = bfs.BFS()
    astarAI = astar.AStarNick()
    backtrackingAI = back_tracking.BackTrackSolver()
    print "5x5 5 colors"
    print "backtracking:", time_run(backtrackingAI.solve, firstFlow, 100)
    print "bfs:", time_run(bfsAI.solve_single_gp, firstFlow, 1)
    print "astar:", time_run(astarAI.solve, firstFlow, 1)
    print

    backtrackingAI = back_tracking.BackTrackSolver()
    print "7x7 "
    print "backtracking:", time_run(backtrackingAI.solve, hardFlow, 100)
    print

    backtrackingAI = back_tracking.BackTrackSolver()
    print "9x9"
    print "backtracking:", time_run(backtrackingAI.solve, hardestFlow, 1)




