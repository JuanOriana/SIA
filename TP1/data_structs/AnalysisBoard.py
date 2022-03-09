from TP1.data_structs import SearchableNode
import time


class AnalysisBoard:
    def __init__(self, success: bool = False, start_node: SearchableNode = None,
                 end_node: SearchableNode = None, expanded_count=0, frontier_count=0, processing_time: time = None):
        self.success = success
        self.start_node = start_node
        self.end_node = end_node
        self.expanded_count = expanded_count
        self.frontier_count = frontier_count
        self.time = time

    def __str__(self):
        if self.success:
            return "SUCCESS! \n Start state ->" + str(self.start_node.state) + "\n" + "End state ->" + str(self.end_node.state) + "\n" + "End depth: " + str(self.end_node.depth) + "\n" + "End cost: " + str(self.end_node.cost) + "\n" + "Time elapsed: " + str(self.time) + "\n" + "Expanded count: " + str(self.expanded_count) + "\n" +"Frontier count: " + str(self.frontier_count)
        else:
            return "FAILED :("