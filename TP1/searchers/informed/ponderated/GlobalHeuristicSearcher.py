from TP1.searchers.informed.ponderated.PonderatedInformedSearcher import PonderatedInformedSearcher


class GlobalHeuristicSearcher(PonderatedInformedSearcher):
    """
      A class that represents an InformedSearcher that implements the Global Heursitic algorithm.
      This algorithm DOES contemplate backtracking.

    """
    def __init__(self, heuristic):
        super().__init__(heuristic, 1)
