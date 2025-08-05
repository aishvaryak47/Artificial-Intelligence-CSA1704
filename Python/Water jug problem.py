from collections import deque

def is_goal(state, goal):
    return goal in state

def get_successors(state, a_cap, b_cap):
    x, y = state
    return set([
        (a_cap, y),       # Fill Jug A
        (x, b_cap),       # Fill Jug B
        (0, y),           # Empty Jug A
        (x, 0),           # Empty Jug B
        (max(0, x - (b_cap - y)), min(b_cap, y + x)),  # Pour A -> B
        (min(a_cap, x + y), max(0, y - (a_cap - x)))   # Pour B -> A
    ])

def water_jug_solver(a_cap, b_cap, goal):
    visited = set()
    queue = deque()
    queue.append(((0, 0), []))

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        if is_goal((x, y), goal):
            return path
        for state in get_successors((x, y), a_cap, b_cap):
            queue.append((state, path))
    return None

# User input
a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
goal = int(input("Enter the goal amount of water: "))

result = water_jug_solver(a, b, goal)

# Output
if result:
    print("\nSteps to reach the goal:")
    for step in result:
        print(step)
    print("\n✅ Goal Reached!")
else:
    print("❌ Goal cannot be reached with given jug capacities.")
