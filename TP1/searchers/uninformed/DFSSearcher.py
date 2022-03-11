from TP1.data_structs.SearchableNode import SearchableNode
from TP1.searchers.Searcher import Searcher


class DFSSearcher(Searcher):

    def solve_internal(self):
        self.frontier.append(self.start_node)
        while self.frontier:
            node = self.frontier.pop()
            self.analytics.expanded_count += 1
            self.visited.add(node.state)
            for new_state in node.possible_moves():
                if new_state not in self.visited:
                    new_node = SearchableNode(new_state, node, node.depth + 1, node.cost + 1)
                    if new_state.is_solved():
                        return new_node
                    self.frontier.append(new_node)
        return None