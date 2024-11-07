import math

def alpha_beta(depth, node, maximizing_player, alpha, beta):
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if maximizing_player:
        max_eval = -math.inf
        for child in get_children(node):
            eval = alpha_beta(depth - 1, child, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in get_children(node):
            eval = alpha_beta(depth - 1, child, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_children(node):
    return node['children']

def evaluate(node):
    return node['value']

def is_terminal(node):
    return node['is_terminal']

def best_move(root, depth):
    best_val = -math.inf
    best_move = None
    for child in get_children(root):
        move_val = alpha_beta(depth, child, False, -math.inf, math.inf)
        if move_val > best_val:
            best_val = move_val
            best_move = child
    return best_move

root = {
    'children': [
        {'children': [], 'value': 3, 'is_terminal': True},
        {'children': [], 'value': 5, 'is_terminal': True},
        {'children': [], 'value': 2, 'is_terminal': True},
        {'children': [], 'value': 9, 'is_terminal': True}
    ],
    'is_terminal': False
}

depth = 3
best = best_move(root, depth)
print("Best move value:", best['value'])
