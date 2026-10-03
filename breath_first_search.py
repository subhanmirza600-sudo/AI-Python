# -----------------------------------------
# BREADTH FIRST SEARCH (BFS)
# -----------------------------------------

from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start, goal):

    # BFS uses a QUEUE.
    #
    # A queue follows FIFO:
    # First In -> First Out
    queue = deque([start])

    # Keep track of visited nodes.
    visited = set()

    while queue:

        # Remove the FIRST node from the queue.
        current = queue.popleft()

        # Don't process a node twice.
        if current in visited:
            continue

        # Mark current node as visited.
        visited.add(current)

        print("Visiting:", current)

        # Check if we reached the goal.
        if current == goal:
            print("Goal found!")
            return

        # Add all neighbors to the queue.
        for neighbor in graph[current]:

            if neighbor not in visited:
                queue.append(neighbor)

    print("Goal not found!")


# Search from A to F
bfs(graph, 'A', 'F')