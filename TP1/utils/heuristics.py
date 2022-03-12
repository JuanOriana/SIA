
from TP1.data_structs.EightState import EightState
import numpy as np

flattened_solved = np.asarray(EightState.finished_state).flatten()


def basic_heuristic(state: EightState) -> int:
    """Heursitic that evaluates how many numbers are out of place. It is admissible"""
    estimation = 0
    width, height = state.width, state.height
    for x in range(width):
        for y in range(height):
            estimation += 1 if state.board[x, y] != EightState.finished_state[x, y] else 0
    return estimation


def deep_heuristic(state: EightState) -> int:
    """Heursitic that evaluates the manhattan distance from each number to its adequate place. It is admissible"""
    estimation = 0
    width, height = state.width, state.height
    for x in range(width):
        for y in range(height):
            if state.board[x, y] != 0:
                n = state.board[x, y]
                actual_x, actual_y = (n - 1) // 3, (n + 2) % 3
                estimation += abs(actual_x - x) + abs(actual_y - y)
    return estimation


def fat_heuristic(state: EightState) -> int:
    """
        Heursitic that evaluates how many numbers are out of place and then squares it.
        Its faster than a basic_heuristic in some cases but it is not admissible.
    """
    basic_estimation = basic_heuristic(state)
    return basic_estimation**2
