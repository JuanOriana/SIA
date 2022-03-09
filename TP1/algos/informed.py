from TP1.data_structs.Searchable import Searchable
from queue import PriorityQueue

def hill_climbing_local(start: Searchable, heuristic):
    next = start
    visited = set()
    while next:
        visited.add(next)
        if next.is_solved():
            print("SOLVED!!")
            print(next)
            return
        possible_moves = next.possible_moves()
        possible_moves.sort(key=heuristic)
        next = None
        for move in possible_moves:
            if move not in visited:
                next = move
                if next.is_solved():
                    print("SOLVED!!")
                    print(next)
                    return
                break

def hill_climbing_global(start: Searchable, heuristic):
    possible_next_queue = PriorityQueue()
    possible_next_queue.put((heuristic(start),start))
    visited = set()
    while possible_next_queue:
        next = possible_next_queue.get()[1]
        if next not in visited:
            visited.add(next)
            possible_moves = next.possible_moves()
            for move in possible_moves:
                if move.is_solved():
                    print("SOLVED!!")
                    print(next)
                    return
                possible_next_queue.put((heuristic(move),move))
