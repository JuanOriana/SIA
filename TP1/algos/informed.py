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


def hill_climbing_global(start: Searchable, heuristic):
    start_h = heuristic(start)
    start_node = SearchableNode(start, estimation=start_h)
    possible_next_queue = PriorityQueue()
    if start_node.state.is_solved():
        print("SOLVED!!")
        solve_path(start_node)
        return
    possible_next_queue.put((start_h, start_node))
    visited = set()
    while possible_next_queue:
        node = possible_next_queue.get()[1]
        visited.add(node.state)
        for move in node.possible_moves():
            if move not in visited:
                move_h = heuristic(move)
                next_node = SearchableNode(move, node, node.depth + 1, node.cost + 1, move_h)
                if move.is_solved():
                    print("SOLVED!!")
                    solve_path(next_node)
                    return
                possible_next_queue.put((move_h, next_node))
