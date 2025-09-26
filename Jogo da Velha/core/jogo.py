from .logica import jogadas_livres, empate, checar_vencedor
from .ia import jogada_ia
from utils.helpers import input_jogador, escolher_rounds, clear_screen
from shutil import get_terminal_size
from utils.print_big_board import imprimir_tabuleiro
import time

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

def rodada_unica(modo, dificuldade=None, jogador_inicial="X", rodada_atual = 1, rodadas_totais = 1):
    jogo = [" "] * 9
    jogador = jogador_inicial
    imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)

    while True:
        ganhador, highlight = checar_vencedor(jogo)
        if ganhador:
            clear_screen()
            print(f"\n--- Rodada {rodada_atual} de {rodadas_totais} ---")
            imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)
            print(f"Vencedor da rodada: {ganhador}")
            time.sleep(5)
            return ganhador
        if empate(jogo):
            clear_screen()
            print(f"\n--- Rodada {rodada_atual} de {rodadas_totais} ---")
            imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)
            print("Rodada terminou em empate.")
            time.sleep(5)
            return "Empate"

        if modo == "PvP":
            mv = input_jogador(jogador)
            if mv == "quit":
                return "Quit"
            if jogo[mv] != " ":
                print("Posição ocupada.")
                continue
            jogo[mv] = jogador
            clear_screen()
            print(f"\n--- Rodada {rodada_atual} de {rodadas_totais} ---")
            imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)
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
                clear_screen()
                print(f"\n--- Rodada {rodada_atual} de {rodadas_totais} ---")
                imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)
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
                clear_screen()
                print(f"\n--- Rodada {rodada_atual} de {rodadas_totais} ---")
                imprimir_tabuleiro(jogo, destaque=None, centralizar_vertical=True)
                jogador = "X"


def serie_de_rodadas(modo, dificuldade=None):
    rodadas = escolher_rounds()
    if rodadas == None:
        return None
    vitorias = {"X": 0, "O": 0, "Empate": 0}
    rodadas_necessarias = int(rodadas) // 2 + 1
    current_start = "X"

    for r in range(1, rodadas + 1):
        clear_screen()
        print(f"\n--- Rodada {r} de {rodadas} ---")
        result = rodada_unica(modo, dificuldade, jogador_inicial=current_start, rodada_atual = r, rodadas_totais = rodadas)

        if result == "Quit":
            print("Jogo interrompido pelo usuario. Voltando ao menu...")
            time.sleep(5)
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
        time.sleep(2)
    elif vitorias["O"] > vitorias["X"]:
        print(
            f"\n=== Serie encerrada: Vencedor: O ({vitorias['O']} x {vitorias['X']}) ==="
        )
        time.sleep(2)
    else:
        print(
            f"\n=== Serie encerrada: Empate na serie ({vitorias['X']} x {vitorias['O']}) ==="
        )
        time.sleep(2)
