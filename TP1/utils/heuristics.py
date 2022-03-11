import math

from TP1.data_structs.EightState import EightState
import numpy as np

flattened_solved = np.asarray(EightState.finished_state).flatten()


def basic_heuristic(state: EightState) -> int:
    estimation = 0
    width, height = state.width, state.height
    for x in range(width):
        for y in range(height):
            estimation += 1 if state.board[x, y] != EightState.finished_state[x, y] else 0
    return estimation


def deep_heuristic(state: EightState) -> int:
    estimation = 0
    width, height = state.width, state.height
    for x in range(width):
        for y in range(height):
            if state.board[x, y] != 0:
                n = state.board[x, y]
                actual_x, actual_y = (n - 1) // 3, (n + 2) % 3
                estimation += abs(actual_x - x) + abs(actual_y - y)
                # estimation += math.sqrt((actual_x-x)**2 + (actual_y-y)**2)
    return estimation


def fat_heuristic(state: EightState) -> int:
    return 2 * basic_heuristic(state)
