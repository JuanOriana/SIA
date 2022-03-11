import numpy as np
import json

from TP1.data_structs.EightState import EightState
from TP1.utils.json_validator import json_validator
from TP1.utils.searcher_picker import heuristics_functions, searcher_picker


def main():

    # TODO: Chequear bpa y bpp si son los correctos en este caso
    input_file = open('input.json')
    data = json.load(input_file)

    json_information = json_validator(data)

    if not json_information['is_valid']:
        return

    # matrix = [[6, 8, 4], [3, 5, 7], [0, 1, 2]]
    matrix = json_information['matrix']

    board = EightState(np.matrix(matrix, dtype=int))

    searcher = searcher_picker(json_information['algorithm_name'], heuristics_functions[json_information['heuristic']])
    searcher.solve(board)
    print(searcher.analytics)


if __name__ == "__main__":
    main()
