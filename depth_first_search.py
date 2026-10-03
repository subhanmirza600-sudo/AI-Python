# -----------------------------------------
# DEPTH FIRST SEARCH (DFS)
# -----------------------------------------

# Our graph.
# Each key represents a node.
# The list contains the nodes connected to it.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# DFS function
def dfs(graph, start, goal):

    # Stack is used in DFS.
    # A stack follows LIFO:
    # Last In -> First Out
    stack = [start]

    # We keep track of nodes that we have already visited.
    visited = set()

    while stack:

        # Remove the LAST node from the stack.
        current = stack.pop()

        # If we have already visited this node,
        # don't process it again.
        if current in visited:
            continue

        # Mark the node as visited.
        visited.add(current)

        print("Visiting:", current)

        # Check whether we reached our goal.
        if current == goal:
            print("Goal found!")
            return

        # Add the neighboring nodes to the stack.
        #
        # reversed() is used here only to make
        # the traversal order easier to understand.
        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)

    print("Goal not found!")


# Start DFS from A and search for F
dfs(graph, 'A', 'F')