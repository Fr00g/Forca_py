import os

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

def choose_mode():
    print("====Jogo da Velha====")
    print("1 - Multiplayer (PvP)")
    print("2 - Contra a máquina (PvE)")
    print("Q - Sair")

    while True:
        escolha = (input('Escolha o modo (1/2) ou Q para sair')).strip().upper()
        
        if escolha == '1':
            return 'PvP'
        elif escolha == '2':
            return 'PvE'
        elif escolha == 'Q':
            return 'Quit'
        else:
            print("Escolha inválida! Tente novamente...")

def choose_rounds():
    while True:
        pick = input('Escolha o número de rodadas (1, 3, 5, 7): ').strip()
        if pick in '1357':
            return int(pick)
        else:
            print('Escolha inválida! Tente novamente...')

def choose_difficulty():
    difficultys = {1: 'Fácil', 2: 'Médio', 3: 'Difícil', 4:'Impossível'}
    print('Níveis da máquina:')
    print('1 - Fácil')
    print('2 - Médio')
    print('3 - Difícil')
    print('4 - Impossível')
    while True:
        pick = input('Escolha o nível (1 - 4): ').strip()
        if pick in difficultys:
            return difficultys[pick]
        else:
            print('Escolha inválida! Tente novamente...')

def player_input_prompt(sinal):
    while True:
        pos = input(f'Jogador {sinal}, escolha uma posição (1 - 9): ')
        if pos in '123456789':
            return int(pos) - 1
        else:
            print('Entrada Inválida! Tente novamente...')
