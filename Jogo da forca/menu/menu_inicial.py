from core.jogo import iniciar_jogo_pvp, iniciar_jogo_ia

def menu():
    print("\n======== JOGO DA VELHA ========")
    print("1. Modo jogador contra jogador (PvP)")
    print("2. Modo jogador contra IA (PvE)")
    print("3. Sair do jogo")
    
    
    while True:
        escolha = int(input("Escolha uma opção (1, 2 ou 3): "))

        if escolha == 1:
            iniciar_jogo_pvp()
    
        elif escolha == 2:
            iniciar_jogo_ia()
        
        elif escolha == 3:
            print("Saindo.........") 
            break
      
        else:
            print("Opção Inválida, tente de novo")
        
        
menu()