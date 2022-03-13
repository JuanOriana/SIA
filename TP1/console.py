import numpy as np
import json
import sys

from TP1.data_structs.EightState import EightState
from TP1.utils.json_validator import json_validator, file_validator
from TP1.utils.searcher_picker import heuristics_functions, searcher_picker


def main():
    if len(sys.argv) != 2:
        print("Invalid usage: console.py <config.json>")
        quit(1)

    json_information = file_validator(sys.argv[1])

    searcher = searcher_picker(json_information['algorithm_name'], heuristics_functions[json_information['heuristic']])
    print("Thinking...")
    searcher.solve(EightState(np.matrix(json_information['matrix'], dtype=int)))
    print(searcher.analytics)


if __name__ == "__main__":
    main()
