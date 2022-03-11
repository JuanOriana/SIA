import time
from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.Searchable import Searchable
from TP1.data_structs.SearchableNode import SearchableNode
from TP1.utils.visualization import solve_path


class Searcher:

    def __init__(self):
        self.frontier = []
        self.visited = set()
        self.analytics = AnalysisBoard()
        self.start_node = None

    def solve(self, start: Searchable) -> []:

        self.set_up(start)

        if start.is_solved():
            self.analytics.success = True
            self.analytics.end_node = self.start_node
            return self.analytics

        start_timer = time.time()
        end_node = self.solve_internal()
        self.analytics.time = time.time() - start_timer

        if end_node:
            self.analytics.success = True
            self.analytics.end_node = end_node
            self.analytics.frontier_count = self.get_frontier_length()
            # because of the state I just added
            self.analytics.expanded_count += 1

        return self.analytics

    def solve_internal(self):
        pass

    def set_up(self, start):
        self.start_node = SearchableNode(start)
        self.analytics = AnalysisBoard(start_node=self.start_node)
        self.frontier = []
        self.visited = set()

    def get_frontier_length(self):
        return len(self.frontier)