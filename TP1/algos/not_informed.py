from TP1.data_structs.AnalysisBoard import AnalysisBoard
from TP1.data_structs.Searchable import Searchable
from TP1.data_structs.SearchableNode import SearchableNode
from TP1.utils.visualization import solve_path


def dfs(start: Searchable):  # function for dfs
    start_node = SearchableNode(start)
    analysis_board = AnalysisBoard(start_node=start_node)
    if start_node.state.is_solved():
        print("SOLVED!!")
        analysis_board.success = True
        analysis_board.end_node = start_node
        solve_path(start_node)
        return analysis_board

    stack = [start_node]
    visited = set()

    while stack:
        node = stack.pop()
        analysis_board.expanded_count += 1
        visited.add(node.state)
        for new_state in node.possible_moves():
            if new_state not in visited:
                new_node = SearchableNode(new_state, node, node.depth + 1, node.cost + 1)
                if new_state.is_solved():
                    print("SOLVED!!")
                    analysis_board.success = True
                    analysis_board.end_node = new_node
                    analysis_board.frontier_count = len(stack)
                    # because of the state I just added
                    analysis_board.expanded_count += 1
                    solve_path(new_node)
                    return analysis_board
                stack.append(new_node)

    return analysis_board


def bfs(start: Searchable):  # function for BFS
    start_node = SearchableNode(start)
    analysis_board = AnalysisBoard(start_node=start_node)
    if start_node.state.is_solved():
        print("SOLVED!!")
        analysis_board.success = True
        analysis_board.end_node = start_node
        solve_path(start_node)
        return analysis_board
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        visited.add(node.state)
        analysis_board.expanded_count += 1
        for new_state in node.possible_moves():
            if new_state not in visited:
                new_node = SearchableNode(new_state, node, node.depth + 1, node.cost + 1)
                if new_state.is_solved():
                    print("SOLVED!!")
                    analysis_board.success = True
                    analysis_board.end_node = new_node
                    analysis_board.frontier_count = len(queue)
                    # because of the state I just added
                    analysis_board.expanded_count += 1
                    solve_path(new_node)
                    return analysis_board
                queue.append(new_node)



