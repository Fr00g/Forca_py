from .logica import print_jogo, jogadas_livres, empate, checar_vencedor
from .ia import jogada_ia
from utils.helpers import input_jogador, escolher_rounds


def rodada_unica(modo, dificuldade=None, jogador_inicial="X"):
    jogo = [" "] * 9
    jogador = jogador_inicial
    print_jogo(jogo)

    while True:
        ganhador, highlight = checar_vencedor(jogo)
        if ganhador:
            print_jogo(jogo, highlight)
            print(f"Vencedor da rodada: {ganhador}")
            return ganhador
        if empate(jogo):
            print_jogo(jogo)
            print("Rodada terminou em empate.")
            return "Empate"

        if modo == "PvP":
            mv = input_jogador(jogador)
            if mv == "quit":
                return "Quit"
            if jogo[mv] != " ":
                print("Posição ocupada.")
                continue
            jogo[mv] = jogador
            print_jogo(jogo)
            jogador = "O" if jogador == "X" else "X"

        else:
            if jogador == "X":
                mv = input_jogador("X")
                if mv == "quit":
                    return "Quit"
                if jogo[mv] != " ":
                    print("Posição ocupada.")
                    continue
                jogo[mv] = "X"
                print_jogo(jogo)
                jogador = "O"
            else:
                print("Máquina jogando...")
                mv = jogada_ia(jogo, dificuldade, simbolo_ia="O", simbolo_jogador="X")
                if mv is None:
                    moves = jogadas_livres(jogo)
                    if not moves:
                        continue
                    import random

                    mv = random.choice(moves)
                jogo[mv] = "O"
                print_jogo(jogo)
                jogador = "X"


def serie_de_rodadas(modo, dificuldade=None):
    rodadas = escolher_rounds()
    vitorias = {"X": 0, "O": 0, "Empate": 0}
    rodadas_necessarias = rodadas // 2 + 1
    current_start = "X"

    for r in range(1, rodadas + 1):
        print(f"\n--- Rodada {r} de {rodadas} ---")
        result = rodada_unica(modo, dificuldade, jogador_inicial=current_start)

        if result == "Quit":
            print("Jogo interrompido pelo usuario. Voltando ao menu.")
            return

        if result == "X":
            vitorias["X"] += 1
        elif result == "O":
            vitorias["O"] += 1
        elif result == "Empate":
            vitorias["Empate"] += 1

        print(
            f"Placar atual: Jogador (X) = {vitorias['X']}  Maquina (O) = {vitorias['O']}  Empates = {vitorias['Empate']}"
        )

        if vitorias["X"] >= rodadas_necessarias or vitorias["O"] >= rodadas_necessarias:
            break

        current_start = "O" if current_start == "X" else "X"

    if vitorias["X"] > vitorias["O"]:
        print(
            f"\n=== Serie encerrada: Vencedor: X ({vitorias['X']} x {vitorias['O']}) ==="
        )
    elif vitorias["O"] > vitorias["X"]:
        print(
            f"\n=== Serie encerrada: Vencedor: O ({vitorias['O']} x {vitorias['X']}) ==="
        )
    else:
        print(
            f"\n=== Serie encerrada: Empate na serie ({vitorias['X']} x {vitorias['O']}) ==="
        )
