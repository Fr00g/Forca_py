from .logica import print_board, available_moves, is_full, check_winner
from .ia import ai_choose_move
from utils.helpers import player_input_prompt, choose_rounds


def play_single_round(mode, difficulty=None, starting_player='X'):
    board = [' '] * 9
    current = starting_player
    print_board(board)

    while True:
        winner, highlight = check_winner(board)
        if winner:
            print_board(board, highlight)
            print(f'Vencedor da rodada: {winner}')
            return winner
        if is_full(board):
            print_board(board)
            print('Rodada terminou em empate.')
            return 'Empate'

        if mode == 'PvP':
            mv = player_input_prompt(current)
            if mv == 'quit':
                return 'Quit'
            if board[mv] != ' ':
                print('Posição ocupada.')
                continue
            board[mv] = current
            print_board(board)
            current = 'O' if current == 'X' else 'X'

        else:
            if current == 'X':
                mv = player_input_prompt('X')
                if mv == 'quit':
                    return 'Quit'
                if board[mv] != ' ':
                    print('Posição ocupada.')
                    continue
                board[mv] = 'X'
                print_board(board)
                current = 'O'
            else:
                print('Máquina jogando...')
                mv = ai_choose_move(board, difficulty, ai_symbol='O', player_symbol='X')
                if mv is None:
                    moves = available_moves(board)
                    if not moves:
                        continue
                    import random
                    mv = random.choice(moves)
                board[mv] = 'O'
                print_board(board)
                current = 'X'


def play_series(mode, difficulty=None):
    rounds = choose_rounds()
    wins = {'X': 0, 'O': 0, 'Empate': 0}
    needed = rounds // 2 + 1
    current_start = 'X'

    for r in range(1, rounds + 1):
        print(f"\n--- Rodada {r} de {rounds} ---")
        result = play_single_round(mode, difficulty, starting_player=current_start)

        if result == 'Quit':
            print('Jogo interrompido pelo usuário. Voltando ao menu.')
            return

        if result == 'X':
            wins['X'] += 1
        elif result == 'O':
            wins['O'] += 1
        elif result == 'Empate':
            wins['Empate'] += 1

        print(f"Placar atual: Jogador (X) = {wins['X']}  Máquina (O) = {wins['O']}  Empates = {wins['Empate']}")

        if wins['X'] >= needed or wins['O'] >= needed:
            break

        current_start = 'O' if current_start == 'X' else 'X'

    if wins['X'] > wins['O']:
        print(f"\n=== Série encerrada: Vencedor: X ({wins['X']} x {wins['O']}) ===")
    elif wins['O'] > wins['X']:
        print(f"\n=== Série encerrada: Vencedor: O ({wins['O']} x {wins['X']}) ===")
    else:
        print(f"\n=== Série encerrada: Empate na série ({wins['X']} x {wins['O']}) ===")
