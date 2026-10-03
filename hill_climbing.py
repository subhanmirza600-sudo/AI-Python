# -----------------------------------------
# HILL CLIMBING
# -----------------------------------------

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


# Heuristic values.
#
# Smaller value means that the node
# is considered closer to the goal.
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}


def hill_climbing(graph, heuristic, start, goal):

    # Start at the starting node.
    current = start

    while True:

        print(
            "Current node:",
            current,
            "Heuristic:",
            heuristic[current]
        )

        # If we reach the goal, stop.
        if current == goal:
            print("Goal found!")
            return

        # Get the neighbors of the current node.
        neighbors = graph[current]

        # If there are no neighbors,
        # we cannot move anywhere.
        if not neighbors:
            print("No more moves.")
            print("Goal not found.")
            return

        # Find the neighbor with the
        # smallest heuristic value.
        best_neighbor = min(
            neighbors,
            key=lambda node: heuristic[node]
        )

        # Compare the best neighbor with
        # the current node.
        #
        # If the neighbor is NOT better,
        # we are stuck.
        if heuristic[best_neighbor] >= heuristic[current]:

            print("No better neighbor found.")
            print("Hill climbing is stuck.")
            return

        # Move to the better neighbor.
        current = best_neighbor


hill_climbing(
    graph,
    heuristic,
    'A',
    'F'
)