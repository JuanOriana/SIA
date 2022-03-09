import numpy as np

from TP1.data_structs.EightState import EightState
from TP1.algos.not_informed import dfs
from TP1.algos.informed import hill_climbing_global
from TP1.utils.heuristics import basic_heuristic


def main():
    matrix = [[6, 8, 4], [3, 5, 7], [0, 1, 2]]
    if not EightState.is_matrix_solvable(matrix):
        print("This matrix does not correspond to a valid state in the game")
        return
    board = EightState(np.matrix(matrix, dtype=int))
    dfs(board)


if __name__ == "__main__":
    main()
