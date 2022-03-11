from queue import PriorityQueue

from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.SearchableNode import SearchableNode
from TP1.searchers.Searcher import Searcher


class InformedSearcher(Searcher):

    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def set_up(self, start):
        self.start_node = SearchableNode(start, estimation=self.heuristic(start))
        self.analytics = AnalysisBoard(start_node=self.start_node)
        self.frontier = PriorityQueue()
        self.visited = set()

    def get_frontier_length(self):
        return self.frontier.qsize()