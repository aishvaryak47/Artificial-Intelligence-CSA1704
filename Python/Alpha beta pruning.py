def minimax(node, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)


    if is_maximizing_player:
        max_eval = float('-inf')
        for child in generate_children(node):
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for child in generate_children(node):
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval
