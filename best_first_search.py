# -----------------------------------------
# BEST FIRST SEARCH
# -----------------------------------------

import heapq


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# Heuristic values.
#
# Smaller value = estimated closer to goal.
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}


def best_first_search(graph, heuristic, start, goal):

    # Priority queue.
    #
    # The node with the SMALLEST heuristic
    # value will be selected first.
    priority_queue = []

    # Add the starting node.
    #
    # (heuristic value, node)
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()

    while priority_queue:

        # Get the node with the lowest heuristic value.
        h_value, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        print("Visiting:", current,
              "Heuristic:", h_value)

        # Check whether we reached the goal.
        if current == goal:
            print("Goal found!")
            return

        # Add neighboring nodes to priority queue.
        for neighbor in graph[current]:

            if neighbor not in visited:

                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal not found!")


best_first_search(
    graph,
    heuristic,
    'A',
    'F'
)