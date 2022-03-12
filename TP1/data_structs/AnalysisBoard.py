from TP1.data_structs import SearchableNode
import time


class AnalysisBoard:
    """
    A class to represent the analytics of a search result.


    Attributes
    ----------
    success : bool
        result of the search
    start_node : SearchableNode
        root node of the search
    end_node : SearchableNode
        last node of the found path
    expanded_count : int
        amount of expanded nodes in search
    frontier_count : int
        amount of nodes in frontier at the last step
    time: time
        lapse of execution

    """

    def __init__(self, success: bool = False, start_node: SearchableNode = None,
                 end_node: SearchableNode = None, expanded_count=0, frontier_count=0, time: time = None):
        self.success = success
        self.start_node = start_node
        self.end_node = end_node
        self.expanded_count = expanded_count
        self.frontier_count = frontier_count
        self.time = time

    def get_path(self):
        """Returns complete path of nodes if found, empty list otherwise"""
        if not self.success:
            return []
        final_order = []
        node = self.end_node
        while node:
            final_order.append(node)
            node = node.parent
        final_order.reverse()
        return final_order

    def __str__(self):
        if self.success:
            return "SUCCESS! \n Start state ->\n" + str(self.start_node.state) + "\n" + "End state ->\n" + str(
                self.end_node.state) + "\n" + "End depth: " + str(self.end_node.depth) + "\n" + "End cost: " + str(
                self.end_node.cost) + "\n" + "Time elapsed: " + str(self.time) + "\n" + "Expanded count: " + str(
                self.expanded_count) + "\n" + "Frontier count: " + str(self.frontier_count)
        else:
            return "FAILED :("
