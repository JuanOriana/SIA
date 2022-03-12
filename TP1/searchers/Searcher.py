import time
from typing import Optional

from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.Searchable import Searchable
from TP1.data_structs.SearchableNode import SearchableNode


class Searcher:
    """
    An interface to represent a searching algorithm for a path finding problem.
    A solve_internal function must be overriden with the adequate algorithm, which has
    a frontier and a visited set to its disposal.


    Attributes
    ----------
    frontier : List
        nodes to be explored
    visited : Set
        nodes visited
    analytics : AnalysisBoard
        end result analytics of search
    start_node : SearchableNode
        current node to begin searching

    """

    def __init__(self):
        self.frontier = []
        self.visited = set()
        self.analytics = AnalysisBoard()
        self.start_node = None

    def solve(self, start: Searchable) -> []:
        """Attempts to find a valid goal based on a starting state"""

        self.set_up(start)

        start_timer = time.time()

        if start.is_solved():
            self.analytics.success = True
            self.analytics.end_node = self.start_node
            self.analytics.time = time.time() - start_timer
            return self.analytics

        end_node = self.solve_internal()
        self.analytics.time = time.time() - start_timer

        if end_node:
            self.analytics.success = True
            self.analytics.end_node = end_node
            self.analytics.frontier_count = self.get_frontier_length()
            # because of the state I just added
            self.analytics.expanded_count += 1

        return self.analytics

    def solve_internal(self) -> Optional[SearchableNode]:
        pass

    def set_up(self, start):
        self.start_node = SearchableNode(start)
        self.analytics = AnalysisBoard(start_node=self.start_node)
        self.frontier = []
        self.visited = set()

    def get_frontier_length(self):
        return len(self.frontier)