from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def get_successors(state):
    successors = []
    m, c, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    for dm, dc in moves:
        if boat == 1:  # Boat on left
            new_state = (m - dm, c - dc, 0)
        else:  # Boat on right
            new_state = (m + dm, c + dc, 1)
        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and is_valid(new_state[0], new_state[1]):
            successors.append(new_state)
    return successors

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    visited = set()
    queue = deque([(start, [])])
    
    while queue:
        (state, path) = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path + [state]
        for succ in get_successors(state):
            queue.append((succ, path + [state]))

solution = solve()
for step in solution:
    print(step)
