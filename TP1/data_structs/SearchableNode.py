from TP1.data_structs.Searchable import Searchable


class SearchableNode(Searchable):

    def __init__(self, state: Searchable, parent=None, depth=0, cost=0, estimation=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.estimation = estimation

    def possible_moves(self) -> []:
        return self.state.possible_moves()

    def is_solved(self) -> bool:
        return self.state.is_solved()
