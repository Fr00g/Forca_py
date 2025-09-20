from core.jogo import serie_de_rodadas
from utils.helpers import escolher_modo, escolher_dificuldade, clear_screen

def menu():
    
    while True:
        clear_screen()
        modo = escolher_modo()

        if modo == 'PvP':
            print("Modo PvP selecionado!")
            serie_de_rodadas(modo = 'PvP')
    
        elif modo == 'PvE':
            print("Modo PvE selecionado!")
            dificuldade = escolher_dificuldade()
            print(f"Nível escolhido: {dificuldade}")
            serie_de_rodadas(modo = 'PvE', dificuldade =  dificuldade)
        
        else:
            print("Saindo.........") 
            break