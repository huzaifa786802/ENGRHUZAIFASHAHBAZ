import heapq
import matplotlib.pyplot as plt
import numpy as np
class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position  # (row, col)
        self.g = g  # Cost from start to node
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost
        self.parent = parent
    def __lt__(self, other):
        return self.f < other.f
def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, Node(start, g=0, h=heuristic(start, goal)))
    closed_set = set()
    node_map = {}
    while open_set:
        current = heapq.heappop(open_set)
        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Reverse path
        closed_set.add(current.position)
        neighbors = get_neighbors(current.position, rows, cols)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_set:
                continue
            g = current.g + 1
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g=g, h=h, parent=current)
            if neighbor in node_map and g >= node_map[neighbor].g:
                continue
            node_map[neighbor] = neighbor_node
            heapq.heappush(open_set, neighbor_node)
    return None  # No path found
def get_neighbors(pos, rows, cols):
    r, c = pos
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    neighbors = [(r+dr, c+dc) for dr, dc in moves]
    return [(nr, nc) for nr, nc in neighbors if 0 <= nr < rows and 0 <= nc < cols]
def visualize_grid(grid, path, start, goal):
    grid = np.array(grid)
    for r, c in path:
        if (r, c) != start and (r, c) != goal:
            grid[r][c] = 3  # Path color
    grid[start[0]][start[1]] = 4
    grid[goal[0]][goal[1]] = 5
    plt.figure(figsize=(6, 6))
    cmap = plt.cm.get_cmap('Accent', 6)
    plt.imshow(grid, cmap=cmap, origin='upper')
    plt.xticks(range(grid.shape[1]))
    plt.yticks(range(grid.shape[0]))
    plt.grid(True)
    plt.title("A* Pathfinding Visualization")
    plt.show()
# Example Usage
def main():
    rows, cols = 10, 10
    start = (0, 0)
    goal = (9, 9)
    obstacles = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)]
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for r, c in obstacles:
        grid[r][c] = 1
    path = astar(grid, start, goal)
    if path:
        print("Shortest path:", path)
        visualize_grid(grid, path, start, goal)
    else:
        print("No path found.")
if __name__ == "__main__":
    main()