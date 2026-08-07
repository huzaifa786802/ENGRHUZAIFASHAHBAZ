# Define a simple graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
# Define heuristic values for each node (lower means closer to goal)
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 6,
    'F': 2,
    'G': 1
}
def best_first_search(start, goal): 
    visited = [] 
    path = [] 
    queue = [(start, heuristic[start])] 
    while queue: 
        # Sort queue based on heuristic value (lowest first) 
        queue.sort(key=lambda x: x[1]) 
        current, _ = queue.pop(0) 
        if current in visited: 
            continue 
        visited.append(current) 
        path.append(current) 
        if current == goal: 
            break 
        for neighbor in graph[current]: 
            if neighbor not in visited: 
                queue.append((neighbor, heuristic[neighbor])) 
    return path
# Run best first search from 'A' to 'G'
result_path = best_first_search('A', 'G')
print("Path found by Best First Search:", result_path)