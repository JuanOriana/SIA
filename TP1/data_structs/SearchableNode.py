from TP1.data_structs.Searchable import Searchable


class SearchableNode(Searchable):

    def __init__(self, state: Searchable, parent=None, depth=0, cost=0, estimation=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.estimation = estimation

    def possible_moves(self) -> []:
        return self.state.possible_moves();

    def is_solved(self) -> bool:
        return self.state.is_solved()

    def __cmp__(self, other):
        return self.state == other.state

    def __eq__(self, other):
        return self.__cmp__(other)

    def __ne__(self, other):
        return not self.__cmp__(other)

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash(self.state)
