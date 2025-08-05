import itertools

def tsp_brute_force(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    
    min_path = None
    min_cost = float('inf')
    
    for perm in itertools.permutations(vertices):
        cost = 0
        k = start
        for j in perm:
            cost += graph[k][j]
            k = j
        cost += graph[k][start]
        
        if cost < min_cost:
            min_cost = cost
            min_path = (start,) + perm + (start,)
    
    return min_path, min_cost

# Example graph as adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_brute_force(graph, 0)
print("Shortest Path:", path)
print("Minimum Cost:", cost)
