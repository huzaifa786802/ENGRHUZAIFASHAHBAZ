import heapq
def best_first_search(graph, start, goal, heuristic):
    # Priority queue with (priority, node, path) tuples
    # Priority is the heuristic value (lower is better)
    open_list = [(heuristic(start), start, [start])]
    # Set of visited nodes
    closed_set = set()
    while open_list:
        # Get the node with the lowest heuristic value
        _, current, path = heapq.heappop(open_list)
        # Check if we've reached the goal
        if current == goal:
            return path, closed_set
        # Skip if we've already visited this node
        if current in closed_set:
            continue
        # Mark as visited
        closed_set.add(current)
        # Add neighbors to the queue
        for neighbor, _ in graph.get(current, []):
            if neighbor not in closed_set:
                # Create a new path with the neighbor
                new_path = path + [neighbor]
                # Add to queue with priority = heuristic value
                heapq.heappush(open_list, (heuristic(neighbor), neighbor, new_path))
    # No path found
    return None, closed_set
# Example usage based on the path in the image ['A', 'C', 'B', 'G']
if __name__ == "__main__":
    # Example graph represented as an adjacency list with edge weights
    # {node: [(neighbor1, weight1), (neighbor2, weight2), ...]}
    graph = {
        'A': [('B', 4), ('C', 3)],
        'B': [('A', 4), ('C', 5), ('D', 5), ('G', 6)],
        'C': [('A', 3), ('B', 5), ('D', 2), ('E', 4)],
        'D': [('B', 5), ('C', 2), ('E', 3), ('F', 4)],
        'E': [('C', 4), ('D', 3), ('F', 6)],
        'F': [('D', 4), ('E', 6), ('G', 3)],
        'G': [('B', 6), ('F', 3)]
    }
    # Example heuristic function (straight-line distance to goal 'G')
    # In a real scenario, this would be calculated based on actual coordinates
    heuristic_values = {
        'A': 7,
        'B': 6,
        'C': 5,
        'D': 4,
        'E': 3,
        'F': 2,
        'G': 0
    }
    def heuristic(node):
        return heuristic_values[node]
    # Run Best-First Search
    start_node = 'A'
    goal_node = 'G'
    path, explored = best_first_search(graph, start_node, goal_node, heuristic)
    # Print results
    print(f"Path found: {path}")
    print(f"Nodes explored: {explored}")
    # Verify if it matches the expected path from the image
    expected_path = ['A', 'C', 'B', 'G']
    print(f"Expected path from image: {expected_path}")
    print(f"Does the algorithm produce the expected path? {path == expected_path}")
    # If paths don't match, we can analyze why
    if path != expected_path:
        print("\nNote: The actual path found may differ from the expected path in the image.")
        print("This can happen because:")
        print("1. Best-First Search doesn't guarantee the shortest path")
        print("2. The actual graph structure and heuristic values affect the search path")
        print("3. The path in the image might be from a different graph or heuristic function")