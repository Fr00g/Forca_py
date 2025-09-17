from core.jogo import play_series
from utils.helpers import choose_mode, choose_difficulty, clear_screen

def menu():
    
    while True:
        clear_screen()
        mode = choose_mode()

        if mode == 'PvP':
            print("Modo PvP selecionado!")
            play_series(mode = 'PvP')
    
        elif mode == 'PvE':
            print("Modo PvE selecionado!")
            difficulty = choose_difficulty()
            print(f"Nível escolhido: {difficulty}")
            play_series(mode = 'PvE', difficulty = difficulty)
        
        else:
            print("Saindo.........") 
            break