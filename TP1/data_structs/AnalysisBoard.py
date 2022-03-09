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
        print("SUCCESS!" if self.success else "FAILED :(")
        if self.success:
            print("Start state ->" + self.start_node.state)
            print("End state ->" + self.end_node.state)
            print("End depth: " + self.end_node.depth)
            print("End cost: " + self.end_node.cost)
            print("Time elapsed: " + self.time)
        print("Expanded count: " + str(self.expanded_count))
        print("Frontier count: " + str(self.frontier_count))
