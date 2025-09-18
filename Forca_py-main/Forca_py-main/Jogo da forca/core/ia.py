import random
from .logica import available_moves, check_winner, is_full


def minimax(board, is_maximizing, ai_symbol, player_symbol):
    winner, _ = check_winner(board)
    if winner == ai_symbol:
        return 1
    elif winner == player_symbol:
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best = -999
        for mv in available_moves(board):
            board[mv] = ai_symbol
            score = minimax(board, False, ai_symbol, player_symbol)
            board[mv] = ' '
            if score > best:
                best = score
        return best
    else:
        best = 999
        for mv in available_moves(board):
            board[mv] = player_symbol
            score = minimax(board, True, ai_symbol, player_symbol)
            board[mv] = ' '
            if score < best:
                best = score
        return best


def best_move_minimax(board, ai_symbol, player_symbol):
    best_score = -999
    best_moves = []
    for mv in available_moves(board):
        board[mv] = ai_symbol
        score = minimax(board, False, ai_symbol, player_symbol)
        board[mv] = ' '
        if score > best_score:
            best_score = score
            best_moves = [mv]
        elif score == best_score:
            best_moves.append(mv)
    return random.choice(best_moves) if best_moves else None


def ai_choose_move(board, difficulty, ai_symbol='O', player_symbol='X'):
    r = random.random()
    if difficulty == 'Fácil':
        return random.choice(available_moves(board))
    elif difficulty == 'Médio':
        if r < 0.5:
            return best_move_minimax(board, ai_symbol, player_symbol)
        else:
            return random.choice(available_moves(board))
    elif difficulty == 'Difícil':
        if r < 0.7:
            return best_move_minimax(board, ai_symbol, player_symbol)
        else:
            return random.choice(available_moves(board))
    elif difficulty == 'Impossível':
        return best_move_minimax(board, ai_symbol, player_symbol)
    else:
        return random.choice(available_moves(board))
