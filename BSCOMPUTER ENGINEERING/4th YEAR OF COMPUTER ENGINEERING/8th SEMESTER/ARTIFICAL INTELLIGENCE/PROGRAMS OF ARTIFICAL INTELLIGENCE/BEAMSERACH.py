# Simple graph (adjacency list)
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []
}
# Heuristic values (lower is better)
heuristic = {
    'A': 5, 'B': 4, 'C': 3, 'D': 6,
    'E': 7, 'F': 2, 'G': 1, 'H': 5, 'I': 4
}
def beam_search(start, goal, beam_width):
    queue = [(start, heuristic[start])]
    path = []
    while queue:
        # Sort nodes based on heuristic (ascending)
        queue.sort(key=lambda x: x[1])
        # Keep top 'beam_width' candidates
        queue = queue[:beam_width]
        next_queue = []
        for current, _ in queue:
            path.append(current)
            if current == goal:
                return path
            for neighbor in graph[current]:
                next_queue.append((neighbor, heuristic[neighbor]))
        queue = next_queue
    return path
# Run beam search with beam width 2
result = beam_search('A', 'G', beam_width=2)
print("Beam Search Path:", result)