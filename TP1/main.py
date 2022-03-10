import numpy as np
import json

from TP1.data_structs.EightState import EightState
from TP1.algos.not_informed import dfs
from TP1.algos.informed import ponderated
from TP1.utils.heuristics import deep_heuristic


def main():
    input_file = open('input.json')
    data = json.load(input_file)
    matrix_from_json = [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]
    # matrix = [[6, 8, 4], [3, 5, 7], [0, 1, 2]]
    matrix = matrix_from_json
    if not EightState.is_matrix_solvable(matrix):
        print("This matrix does not correspond to a valid state in the game")
        return
    board = EightState(np.matrix(matrix, dtype=int))
    anal = dfs(board)
    print(str(anal))


if __name__ == "__main__":
    main()
