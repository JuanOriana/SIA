def dfs(graph, node, visited=None):  # function for dfs
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


def bfs(graph, node):  # function for BFS
    visited = [node]
    queue = [node]

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour
                     )
