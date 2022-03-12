from TP1.searchers.informed.InformedSearcher import InformedSearcher
from TP1.data_structs.SearchableNode import SearchableNode


class LocalHeuristicSearcher(InformedSearcher):
    """
      A class that represents an InformedSearcher for the Local Heuristic optimization algorithm.
      This algorithm does NOT contemplate backtracking.

    """

    name = "Local Heuristic"

    def solve_internal(self):
        next_node = self.start_node
        while next_node:
            self.analytics.expanded_count += 1
            self.visited.add(next_node.state)
            if next_node.is_solved():
                return next_node
            possible_moves = next_node.possible_moves()
            possible_moves.sort(key=self.heuristic)
            parent_node = next_node
            next_node = None
            for move in possible_moves:
                if move not in self.visited:
                    next_node = SearchableNode(move, parent_node, parent_node.depth + 1, parent_node.cost + 1,
                                               self.heuristic(move))
                    break
        return None
