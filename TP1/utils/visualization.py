from TP1.data_structs.SearchableNode import SearchableNode


def solve_path(start_node: SearchableNode):
    final_order = []
    node = start_node
    while node:
        final_order.append(node)
        node = node.parent
    final_order.reverse()
    print("THE END PATH OF DEPTH " + str(start_node.depth) + " IS: \n")
    for traverse_node in final_order:
        print(traverse_node.state)
        print("_______\n")