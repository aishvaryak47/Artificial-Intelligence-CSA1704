import math

# Print the board
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print()

# Check for win
def check_win(board, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cols
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

# Check for draw
def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

# Minimax algorithm
def minimax(board, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = str(i + 1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = str(i + 1)
                best_score = min(score, best_score)
        return best_score

# Find best move for AI
def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game function
def play_game():
    board = [str(i + 1) for i in range(9)]
    print("Welcome to Tic Tac Toe! You are 'X'. AI is 'O'.")

    while True:
        print_board(board)

        # Player move
        move = input("Choose your move (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue
        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("That spot is taken. Try again.")
            continue
        board[move] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("🎉 You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai = best_move(board)
        board[ai] = 'O'
        print(f"AI plays at position {ai + 1}.")

        if check_win(board, 'O'):
            print_board(board)
            print("😞 AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()
