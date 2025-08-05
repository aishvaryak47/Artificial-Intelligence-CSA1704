# Define the map as a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

# Store result
coloring = {}

def is_valid(node, color):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def backtrack(node_list, index):
    if index == len(node_list):
        return True
    node = node_list[index]
    for color in colors:
        if is_valid(node, color):
            coloring[node] = color
            if backtrack(node_list, index + 1):
                return True
            del coloring[node]  # Backtrack
    return False

nodes = list(graph.keys())
if backtrack(nodes, 0):
    print("Coloring Solution:")
    print(coloring)
else:
    print("No solution found.")
