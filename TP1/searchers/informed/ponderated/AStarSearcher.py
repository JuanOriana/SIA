from TP1.searchers.informed.ponderated.PonderatedInformedSearcher import PonderatedInformedSearcher


class AStarSearcher(PonderatedInformedSearcher):
    """
      A class that represents an InformedSearcher that implements the A* algorithm

    """
    name = "A*"

    def __init__(self, heuristic):
        super().__init__(heuristic,0.5)
