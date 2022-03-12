class Searchable:

    """
    Interface for objects that can be searched by a pathfinding algorithm
    """
    def possible_moves(self) -> []:
        """Returns a list of possible moves"""

        pass

    def is_solved(self) -> bool:
        """Returns True if found a node that is a goal, False otherwise"""
        pass
