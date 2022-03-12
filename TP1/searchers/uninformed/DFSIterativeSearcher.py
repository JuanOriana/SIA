
from TP1.data_structs.DeepSearchableNode import DeepSearchableNode
from TP1.searchers.Searcher import Searcher


class DFSIterativeSearcher(Searcher):
    """
      A class that represents a Searcher for the interative version of the DFS algorithm.
      One can define the starting limit for the algorithm, and the maximum amount of iterations.
      The algorithm will then try to scale the limit until it finds a valid solution or it runs out of iterations.

    """
    def __init__(self, start_limit = 12, max_iterations = 5):
        super().__init__()
        self.start_limit = start_limit
        self.max_iterations = max_iterations

    def solve_internal(self):
        limit = self.start_limit
        iterations = self.max_iterations
        solution = None
        while iterations and not solution:
            solution = self.__solve_internal_limited(limit)
            if not solution:
                limit += self.start_limit
            iterations -= 1
        return solution

    def solve_internal_limited(self,limit):
        self.frontier = []
        self.visited = set()
        self.frontier.append(DeepSearchableNode(state=self.start_node.state))
        if self.start_node.is_solved():
            return self.start_node
        while self.frontier:
            node = self.frontier.pop()
            self.analytics.expanded_count += 1
            self.visited.add(node)
            for new_state in node.possible_moves():
                new_node = DeepSearchableNode(new_state, node, node.depth + 1, node.cost + 1)
                if new_node not in self.visited and node.depth + 1 <= limit:
                    if new_state.is_solved():
                        return new_node
                    self.frontier.append(new_node)
        return None
