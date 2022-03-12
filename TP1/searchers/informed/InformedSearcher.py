from queue import PriorityQueue

from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.SearchableNode import SearchableNode
from TP1.searchers.Searcher import Searcher


class InformedSearcher(Searcher):
    """
      An interface to represent a searching algorithm for an INFORMED path finding problem.
      A solve_internal function must be overriden with the adequate algorithm, which has
      a frontier (PriorityQueue!) and a visited set to its disposal.


      Attributes
      ----------
      frontier : PriorityQueue
          nodes to be explored
      visited : Set
          nodes visited
      analytics : AnalysisBoard
          end result analytics of search
      start_node : SearchableNode
          current node to begin searching
      heuristic: (Serachable) -> double
          the heuristic to estimate

    """
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