import numpy as np
import sys

from TP1.data_structs.EightState import EightState
from TP1.utils.json_validator import file_validator
from TP1.utils.searcher_picker import heuristics_functions, searcher_picker


def main():
    if len(sys.argv) != 2:
        print("Invalid usage: console.py <config.json>")
        quit(1)

    json_information = file_validator(sys.argv[1])

    searcher = searcher_picker(json_information['algorithm_name'], heuristics_functions[json_information['heuristic']])
    print("Thinking...\n")
    searcher.solve(EightState(np.matrix(json_information['matrix'], dtype=int)))
    print(searcher.analytics)
    print("Algorithm: " + json_information['algorithm_name'] + "\n")
    ret = input("Do you wish to see all the steps? y/n")
    if ret[0] == 'y' or ret[0] == 'Y':
        path = searcher.analytics.get_path()
        for idx, step in enumerate(path):
            print("Step: " + str(idx))
            print(step.state)
            print("-------------------------")


if __name__ == "__main__":
    main()
