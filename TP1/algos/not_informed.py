from TP1.data_structs.Searchable import Searchable


def dfs(start: Searchable):  # function for dfs
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for new_state in node.possible_moves():
                if new_state.is_solved():
                    print("SOLVED!!")
                    print(new_state)
                    return
                stack.append(new_state)

def bfs(start:Searchable):  # function for BFS
    visited = set()
    queue = [start]

    while queue:  # Creating loop to visit each node
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for new_state in node.possible_moves():
                if new_state.is_solved():
                    print("SOLVED!!")
                    print(new_state)
                    return
                queue.append(new_state)
