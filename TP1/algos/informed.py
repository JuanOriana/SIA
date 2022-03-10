from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.Searchable import Searchable
from queue import PriorityQueue

from TP1.data_structs.SearchableNode import SearchableNode
from TP1.utils.visualization import solve_path


def hill_climbing_local(start: Searchable, heuristic):
    next_node = SearchableNode(start, estimation=heuristic(start))
    visited = set()

    while next_node:
        visited.add(next_node.state)
        if next_node.is_solved():
            print("SOLVED!!")
            solve_path(next_node)
            return
        possible_moves = next_node.possible_moves()
        possible_moves.sort(key=heuristic)
        parent_node = next_node
        next_node = None
        for move in possible_moves:
            if move not in visited:
                next_node = SearchableNode(move, parent_node, parent_node.depth + 1, parent_node.cost + 1,
                                           heuristic(move))
                break


def ponderated(start: Searchable, heuristic, ponderation):
    start_h = heuristic(start)
    start_node = SearchableNode(start, estimation=start_h)
    possible_next_queue = PriorityQueue()
    analysis_board = AnalysisBoard(start_node=start_node)

    if start_node.state.is_solved():
        print("SOLVED!!")
        analysis_board.success = True
        analysis_board.end_node = start_node
        solve_path(start_node)
        return analysis_board
    start_f = 0 * ponderation[0] + start_h * ponderation[1]
    possible_next_queue.put((start_f, start_node))
    visited = set()
    while possible_next_queue:
        analysis_board.expanded_count += 1
        node = possible_next_queue.get()[1]
        visited.add(node.state)
        for move in node.possible_moves():
            if move not in visited:
                move_h = heuristic(move)
                move_g = node.cost + 1
                move_f = move_g * ponderation[0] + move_h * ponderation[1]
                next_node = SearchableNode(move, node, node.depth + 1, move_g, move_h)
                if move.is_solved():
                    print("SOLVED!!")
                    analysis_board.success = True
                    analysis_board.end_node = next_node
                    analysis_board.frontier_count = possible_next_queue.qsize()
                    # because of the state I just added
                    analysis_board.expanded_count += 1
                    solve_path(next_node)
                    return analysis_board
                possible_next_queue.put((move_f, next_node))


def a_star(start: Searchable, heuristic):
    ponderated(start, heuristic, (0.5, 0.5))


def hill_climbing_global(start: Searchable, heuristic):
    ponderated(start, heuristic, (0, 1))
