from collections import deque

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

# BFS Function
def bfs(graph, start, goal):

    # Queue stores paths
    queue = deque([[start]])

    # List to store visited nodes
    visited = []

    while queue:

        # Remove first path from queue
        path = queue.popleft()

        # Get the last node in the path
        node = path[-1]

        # Check if node has not been visited
        if node not in visited:

            visited.append(node)

            # Goal test
            if node == goal:
                print("BFS Search Path:")
                print(" -> ".join(path))
                return

            # Explore neighbors
            for neighbor in graph[node]:

                # Create new path
                new_path = list(path)
                new_path.append(neighbor)

                # Add new path to queue
                queue.append(new_path)

    print("Goal node not found.")

# Driver Code
bfs(graph, 'A', 'G')
