# -----------------------------------------
# BEAM SEARCH
# -----------------------------------------

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': []
}


# Heuristic values.
# Smaller value = considered better.
heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 1,
    'G': 7,
    'H': 0,
    'I': 8
}


def beam_search(graph, heuristic, start, goal, beam_width):

    # At the beginning, our only candidate is START.
    current_level = [start]

    visited = set()

    while current_level:

        print("\nCurrent level:", current_level)

        # Check every node in the current level.
        for node in current_level:

            if node in visited:
                continue

            visited.add(node)

            print("Visiting:", node)

            if node == goal:
                print("Goal found!")
                return

        # Find all children of the current level.
        next_level = []

        for node in current_level:

            for neighbor in graph[node]:

                if neighbor not in visited:
                    next_level.append(neighbor)

        # Sort nodes according to heuristic.
        #
        # Smallest heuristic comes first.
        next_level.sort(
            key=lambda node: heuristic[node]
        )

        # Keep ONLY beam_width number of nodes.
        #
        # For example:
        # beam_width = 2
        #
        # [B, C, D]
        #
        # becomes:
        #
        # [C, D]
        current_level = next_level[:beam_width]

    print("Goal not found!")


beam_search(
    graph,
    heuristic,
    'A',
    'H',
    beam_width=2
)