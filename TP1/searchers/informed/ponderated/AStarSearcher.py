from TP1.searchers.informed.ponderated.PonderatedInformedSearcher import PonderatedInformedSearcher


class AStarSearcher(PonderatedInformedSearcher):

    def __init__(self, heuristic):
        super().__init__(heuristic,0.5)
