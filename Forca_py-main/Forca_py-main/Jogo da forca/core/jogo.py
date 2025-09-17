from .logic import print_board, available_moves, is_full, check_winner
from .ai import ai_choose_move
from utils.helpers import player_input_prompt, choose_rounds


def play_single_round(mode, difficulty = None, starting_player = 'X'):
    board = [' '] * 9
    current = starting_player
    print_board(board)
    while True:
        winner, highlight = check_winner(board)
        if winner:
            print_board(board, highlight)
            print(f'O vencedor da rodada é: {winner}')
            return winner
        
        if is_full(board):
            print_board(board)
            print('Empate!')
            return 'Empate'
    
        if 
    