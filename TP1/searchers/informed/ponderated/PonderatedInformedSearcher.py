from TP1.searchers.informed.InformedSearcher import InformedSearcher
from TP1.data_structs.SearchableNode import SearchableNode


class PonderatedInformedSearcher(InformedSearcher):

    def __init__(self, heuristic, heuristic_weight):
        super().__init__(heuristic)
        self.heuristic_weight = heuristic_weight

    def solve_internal(self):
        ponderation = (1-self.heuristic_weight,self.heuristic_weight)
        start_f = 0 * ponderation[0] + self.start_node.estimation * ponderation[1]
        self.frontier.put((start_f, self.start_node))

        while self.frontier:
            self.analytics.expanded_count += 1
            node = self.frontier.get()[1]
            self.visited.add(node.state)
            for move in node.possible_moves():
                if move not in self.visited:
                    move_h = self.heuristic(move)
                    move_g = node.cost + 1
                    move_f = move_g * ponderation[0] + move_h * ponderation[1]
                    next_node = SearchableNode(move, node, node.depth + 1, move_g, move_h)
                    if move.is_solved():
                        return next_node
                    self.frontier.put((move_f, next_node))
        return None
