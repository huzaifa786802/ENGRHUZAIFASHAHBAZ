from queue import PriorityQueue
from heapq import heappush, heappop
# ---------- Graph Definition ----------
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': [],
    'G': ['M'],
    'H': ['N'],
    'I': ['O'],
    'J': ['P'],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': []
}
# ---------- Heuristic Values (Assumed) ----------
heuristics = {
    'A': 10, 'B': 8, 'C': 7, 'D': 6,
    'E': 5, 'F': 4, 'G': 5, 'H': 6,
    'I': 4, 'J': 5, 'K': 0, 'L': 1,
    'M': 2, 'N': 3, 'O': 2, 'P': 1
}
# ---------- Best First Search (Greedy BFS) ----------
def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], [start]))
    while not pq.empty():
        _, path = pq.get()
        current = path[-1]
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                pq.put((heuristics[neighbor], new_path))
    return None
# ---------- Beam Search ----------
def beam_search(graph, heuristics, start, goal, beam_width):
    queue = [([start], heuristics[start])]
    while queue:
        queue = sorted(queue, key=lambda x: x[1])[:beam_width]
        next_level = []
        for path, _ in queue:
            current = path[-1]
            if current == goal:
                return path
            for neighbor in graph.get(current, []):
                new_path = path + [neighbor]
                cost = heuristics[neighbor]
                heappush(next_level, (new_path, cost))
        queue = next_level
    return None
# ---------- Example Execution ----------
start_node = 'A'
goal_node = 'K'
beam_width = 2
print("Graph:", graph)
print("Heuristics:", heuristics)
print("\nStarting from '{}' to reach '{}'".format(start_node, goal_node))
# Run Best First Search
bfs_result = best_first_search(graph, heuristics, start_node, goal_node)
print("\n Best First Search Path:", bfs_result)
# Run Beam Search
beam_result = beam_search(graph, heuristics, start_node, goal_node, beam_width)
print(" Beam Search Path (Beam Width = {}): {}".format(beam_width, beam_result))