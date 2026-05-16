# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# DFS Function
def dfs(graph, start, goal, path=[]):

    # Add current node to path
    path = path + [start]

    # Goal test
    if start == goal:
        return path

    # Explore neighbors
    for node in graph[start]:

        # Avoid revisiting nodes
        if node not in path:

            new_path = dfs(graph, node, goal, path)

            if new_path:
                return new_path

    return None

# Driver Code
result = dfs(graph, 'A', 'G')

print("DFS Search Path:")
print(" -> ".join(result))
