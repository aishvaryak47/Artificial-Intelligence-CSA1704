import heapq

# Manhattan Distance Heuristic
def manhattan(state, goal):
    dist = 0
    for i in range(1, 9):
        xi, yi = divmod(state.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        dist += abs(xi - xg) + abs(yi - yg)
    return dist

# Generate neighbors (possible next states)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    moves = {
        'up': -3, 'down': 3,
        'left': -1, 'right': 1
    }

    for move, pos in moves.items():
        new_index = index + pos
        if move == 'left' and index % 3 == 0: continue
        if move == 'right' and (index + 1) % 3 == 0: continue
        if 0 <= new_index < 9:
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# A* Search Algorithm
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan(start, goal), 0, start, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                h = manhattan(neighbor, goal)
                heapq.heappush(open_list, (new_g + h, new_g, neighbor, path + [state]))
    return None

# Get user input
def get_state(prompt):
    print(prompt)
    state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        state.extend(row)
    return tuple(state)

# Run the program
start = get_state("Enter the start state (3 rows, 0 for blank):")
goal = get_state("Enter the goal state (3 rows):")

result = astar(start, goal)

# Output
if result:
    print("\n✅ Solution found in", len(result)-1, "moves!")
    for step in result:
        print("\n".join(str(step[i:i+3]) for i in range(0, 9, 3)))
        print("---------")
else:
    print("❌ No solution found.")
