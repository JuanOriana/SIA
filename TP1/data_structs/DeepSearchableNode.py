from TP1.data_structs.SearchableNode import SearchableNode


class DeepSearchableNode(SearchableNode):
    """
    A class to represent the node that takes into account cost for comparisons
    """

    def __cmp__(self, other):
        return self.state == other.state and other.cost >= self.cost

    def __eq__(self, other):
        return self.__cmp__(other)

    def __ne__(self, other):
        return not self.__cmp__(other)

    def __lt__(self, other):
        return False

    def __hash__(self):
        return hash((self.state,self.cost))
