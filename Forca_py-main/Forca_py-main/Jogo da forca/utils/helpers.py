import os
from shutil import get_terminal_size

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass


reset   = "\033[0m"
negrito  = "\033[1m"
vermelho = "\033[31m"
verde    = "\033[32m"
amarelo  = "\033[33m"
azul     = "\033[34m"
magenta  = "\033[35m"
ciano    = "\033[36m"
branco   = "\033[37m"
largura = get_terminal_size().columns

def escolher_modo():
    

    titulo = r"""
   $$$$$\                                           $$\                                      $$\ $$\                 
   \__$$ |                                          $$ |                                     $$ |$$ |                
      $$ | $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$$ | $$$$$$\        $$\    $$\  $$$$$$\  $$ |$$$$$$$\   $$$$$$\  
      $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$ | \____$$\       \$$\  $$  |$$  __$$\ $$ |$$  __$$\  \____$$\ 
$$\   $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |      $$ /  $$ | $$$$$$$ |       \$$\$$  / $$$$$$$$ |$$ |$$ |  $$ | $$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |        \$$$  /  $$   ____|$$ |$$ |  $$ |$$  __$$ |
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$  |      \$$$$$$$ |\$$$$$$$ |         \$  /   \$$$$$$$\ $$ |$$ |  $$ |\$$$$$$$ |
 \______/  \______/  \____$$ | \______/        \_______| \_______|          \_/     \_______|\__|\__|  \__| \_______|
                    $$\   $$ |                                                                                       
                    \$$$$$$  |                                                                                       
                     \______/                                                                                        
    """
    for linha in titulo.splitlines():
        print(f'{negrito}{ciano}{linha.center(largura)}{reset}')

    print(f"{ciano}{"1 - Multiplayer (PvP)".center(largura)}{reset}")
    print(f"{ciano}{"2 - Contra a máquina (PvE)".center(largura)}{reset}")
    print(f"{vermelho}{"Q - Sair".center(largura)}{reset}")

    while True:
        escolha = input(f"\n{amarelo}Escolha o modo (1/2) ou Q para sair: {reset}").strip().upper()
        
        if escolha == '1':
            return 'PvP'
        elif escolha == '2':
            return 'PvE'
        elif escolha == 'Q':
            return 'Quit'
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")

def escolher_rounds():
    titulo = r"""
______          _           _           
| ___ \        | |         | |          
| |_/ /___   __| | __ _  __| | __ _ ___ 
|    // _ \ / _` |/ _` |/ _` |/ _` / __|
| |\ \ (_) | (_| | (_| | (_| | (_| \__ \
  \_| \_\___/ \__,_|\__,_|\__,_|\__,_|___/  
"""
    clear_screen()
    for linha in titulo.splitlines():
        print(f'{negrito}{ciano}{linha.center(largura)}{reset}')

    print(f'\n{verde}{'1 - Melhor de 1'.center(largura)}{reset}')
    print(f'{amarelo}{'2 - Melhor de 3'.center(largura)}{reset}')
    print(f'{magenta}{'3 - Melhor de 5'.center(largura)}{reset}')
    print(f'{vermelho}{'4 - Melhor de 7'.center(largura)}{reset}')
    print('Q - Voltar para o menu'.center(largura))
    
    while True:
        rodadas = input(f'\n{amarelo}Escolha uma opção (1 - 4) ou volte para o menu (Q): {reset}').strip().lower()
        if rodadas in '1234':
            return int(rodadas)
        elif rodadas == 'q':
            return None
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")

def escolher_dificuldade():
    titulo = titulo = r"""
 ______ _  __ _            _     _           _             _____  ___  
|  _  (_)/ _(_)          | |   | |         | |           |_   _|/ _ \ 
| | | |_| |_ _  ___ _   _| | __| | __ _  __| | ___  ___    | | / /_\ \
| | | | |  _| |/ __| | | | |/ _` |/ _` |/ _` |/ _ \/ __|   | | |  _  |
| |/ /| | | | | (__| |_| | | (_| | (_| | (_| |  __/\__ \  _| |_| | | |
|___/ |_|_| |_|\___|\__,_|_|\__,_|\__,_|\__,_|\___||___/  \___/\_| |_/
"""
    clear_screen()
    dificuldades = {'1': 'Fácil', '2': 'Médio', '3': 'Difícil', '4':'Impossível'}
    for linha in titulo.splitlines():
        print(f'{negrito}{ciano}{linha.center(largura)}{reset}')
    print(f'\n{verde}{'1 - Fácil'.center(largura)}{reset}')
    print(f'{amarelo}{'2 - Médio'.center(largura)}{reset}')
    print(f'{magenta}{'3 - Difícil'.center(largura)}{reset}')
    print(f'{vermelho}{'4 - Impossível'.center(largura)}{reset}')
    print('Q - Voltar para o menu'.center(largura))
    while True:
        nivel = input(f'\n{amarelo}Escolha o nível (1 - 4) ou volte para o menu (Q): {reset}').strip().lower()
        if nivel == "q":
            return None
        elif nivel in dificuldades:
            return dificuldades[nivel]
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")

def input_jogador(sinal):
    while True:
        
        pos = input(f'{amarelo}Jogador {sinal}, escolha uma posição (1 - 9), ou saia do jogo (Q): {reset}')
        if pos in '123456789':
            return int(pos) - 1
        elif pos.lower() == 'q':
            return 'quit'
        else:
            print(f"{vermelho}Escolha inválida! Tente novamente...{reset}")
