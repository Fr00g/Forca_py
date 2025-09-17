WINS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def print_board(board, highlight = None):
    print()
    for i in range(3):
        linha = []
        for j in range(3):
            coordenada = 3 * i + j
            cell = board[coordenada]
            if highlight and coordenada in highlight:
                cell = f'-{cell}-'
            linha.append(cell if cell != ' ' else ' ')
        print(' | '.join(linha))
        if i < 2:
            print('----------------')
    print()

def available_moves(board):
return [i for i, v in enumerate(board) if v == ' ']

def is_full(board):
return all(v != ' ' for v in board)

def check_winner(board):
for a,b,c in WINS:
if board[a] == board[b] == board[c] and board[a] != ' ':
return board[a], (a,b,c)
return None, None        