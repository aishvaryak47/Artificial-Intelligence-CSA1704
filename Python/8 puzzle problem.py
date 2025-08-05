import heapq

goal_state = []
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down

def manhattan(state, goal):
    dist = 0
    for i in range(1, 9):
        xi, yi = divmod(state.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        dist += abs(xi - xg) + abs(yi - yg)
    return dist

def is_solvable(puzzle):
    inv = 0
    for i in range(8):
        for j in range(i+1, 9):
            if puzzle[i] and puzzle[j] and puzzle[i] > puzzle[j]:
                inv += 1
    return inv % 2 == 0

def get_neighbors(state):
    i = state.index(0)
    x, y = divmod(i, 3)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ni = nx * 3 + ny
            new_state = state[:]
            new_state[i], new_state[ni] = new_state[ni], new_state[i]
            neighbors.append(new_state)
    return neighbors

def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan(start, goal), 0, start, []))
    visited = set()

    while open_set:
        est, cost, state, path = heapq.heappop(open_set)
        if state == goal:
            return path + [state]
        visited.add(tuple(state))
        for neighbor in get_neighbors(state):
            if tuple(neighbor) not in visited:
                heapq.heappush(open_set, (cost + 1 + manhattan(neighbor, goal), cost + 1, neighbor, path + [state]))
    return None

def get_input_state(prompt):
    print(prompt)
    nums = []
    while len(nums) < 9:
        nums += list(map(int, input(f"Enter remaining {9 - len(nums)} values (0-8): ").split()))
    return nums

# User input
start_state = get_input_state("Enter Initial State (0 represents empty space):")
goal_state = get_input_state("Enter Goal State:")

# Solve
if not is_solvable(start_state):
    print("\nThis puzzle is not solvable.")
else:
    print("\nSolving the puzzle...")
    path = a_star(start_state, goal_state)
    print(f"\nSteps to solve ({len(path)-1} moves):")
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print("---")
