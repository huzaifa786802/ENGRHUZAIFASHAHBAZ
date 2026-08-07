import heapq
# Graph structure: Node -> List of (Neighbor, Cost)
graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []
}
# Heuristic values (h(n))
heuristic = {
    'S': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}
def a_star_search(start, goal):
    open_list = []
    # Push starting node: (f = g + h, g, current_node, path_so_far)
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            print("Path found:", path)
            print("Total cost:", g)
            return path
        for neighbor, cost in graph[current]:
            g_new = g + cost
            f_new = g_new + heuristic[neighbor]
            heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))
    print("No path found.")
    return None
# Run the search from 'S' to 'G'
a_star_search('S', 'G')