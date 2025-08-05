N = 8  

def print_solution(board):
    for row in board:
        for col in row:
            print("Q" if col == 1 else ".", end=" ")
        print()
    print()
def is_safe(board, row, col):
    # Check row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if i < N and board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= N:
        print_solution(board)
        return True                                                   
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0  # BACKTRACK

    return res

# Initialize 8x8 chessboard with all 0s
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve_n_queens(board, 0):
    print("No solution exists.")
