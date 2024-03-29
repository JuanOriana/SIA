from TP1.searchers.informed.LocalHeuristicSearcher import LocalHeuristicSearcher
from TP1.searchers.informed.ponderated.AStarSearcher import AStarSearcher
from TP1.searchers.informed.ponderated.GlobalHeuristicSearcher import GlobalHeuristicSearcher
from TP1.searchers.uninformed.BFSSearcher import BFSSearcher
from TP1.searchers.uninformed.DFSIterativeSearcher import DFSIterativeSearcher
from TP1.searchers.uninformed.DFSSearcher import DFSSearcher
from TP1.utils.heuristics import deep_heuristic, basic_heuristic, fat_heuristic

informed_algorithms = {'a_star': AStarSearcher, 'local_heuristic': LocalHeuristicSearcher,
                       'global_heuristic': GlobalHeuristicSearcher}
not_informed_algorithms = {'bpa': BFSSearcher, 'bpp': DFSSearcher, 'bppv': DFSIterativeSearcher}
heuristics_functions = {'basic': basic_heuristic, 'deep': deep_heuristic, 'fat': fat_heuristic}


def searcher_picker(algo_name, heuristic):
    if informed_algorithms.__contains__(algo_name):
        return informed_algorithms[algo_name](heuristic)

    elif not_informed_algorithms.__contains__(algo_name):
        return not_informed_algorithms[algo_name]()
    else:
        print("ERROR: This algorithm is not valid")

