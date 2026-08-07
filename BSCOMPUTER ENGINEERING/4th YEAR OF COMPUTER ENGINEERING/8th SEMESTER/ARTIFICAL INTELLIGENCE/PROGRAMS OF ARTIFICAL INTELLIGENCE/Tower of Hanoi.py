import matplotlib.pyplot as plt
import networkx as nx
# Define the steps for 3 disks from Tower of Hanoi
steps = [
    ("A", "C", 1),
    ("A", "B", 2),
    ("C", "B", 1),
    ("A", "C", 3),
    ("B", "A", 1),
    ("B", "C", 2),
    ("A", "C", 1),
]
# Create a directed graph
G = nx.DiGraph()
# Add nodes and edges based on the moves
for i, (src, dst, disk) in enumerate(steps, start=1):
    label = f"Move {disk} from {src} to {dst}"
    G.add_node(i, label=label)
    if i > 1:
        G.add_edge(i - 1, i)
# Prepare labels for plotting
labels = nx.get_node_attributes(G, 'label')
# Plotting
plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, labels=labels, node_size=2500, node_color='lightblue', font_size=9, font_weight='bold', arrows=True)
plt.title("Tower of Hanoi - 3 Disks Move Graph")
plt.axis('off')
plt.tight_layout()
plt.show()