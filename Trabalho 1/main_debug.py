import os
import random
import time

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))
    print("\n")

def tabuleiro_valido(tabuleiro):
    # Verifica as linhas
    for linha in tabuleiro:
        linha_set = set()
        for num in linha:
            if num != 0 and num in linha_set:
                return False
            linha_set.add(num)

    # Verifica as colunas
    for coluna in range(9):
        coluna_set = set()
        for linha in range(9):
            num = tabuleiro[linha][coluna]
            if num != 0 and num in coluna_set:
                return False
            coluna_set.add(num)

    # Verifica os quadrantes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrante_set = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    num = tabuleiro[x][y]
                    if num != 0 and num in quadrante_set:
                        return False
                    quadrante_set.add(num)

    return True

def validade(tabuleiro, linha, coluna, num):
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False

    inicio_linha, inicio_coluna = 3 * (linha // 3), 3 * (coluna // 3)

    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == num:
                return False
    return True

def resolver_sudoku(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if validade(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        if resolver_sudoku(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return True

def esta_correto(tabuleiro):
    for i in range(9):
        soma_linha = sum(tabuleiro[i])
        soma_coluna = sum(tabuleiro[j][i] for j in range(9))
        if soma_linha != 45 or soma_coluna != 45:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            soma_quadrante = sum(tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3))
            if soma_quadrante != 45:
                return False

    return True

def ler_sudoku_de_arquivo(nome_arquivo):
    tabuleiro_sudoku = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha_sudoku = [int(x) for x in linha.split()]
            tabuleiro_sudoku.append(linha_sudoku)
    return tabuleiro_sudoku

def resolver_sudoku_com_passo_a_passo(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                for num in range(1, 10):
                    if validade(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        imprimir_tabuleiro(tabuleiro)
                        time.sleep(0.1)  # Ajuste conforme necessário para a visualização
                        if resolver_sudoku_com_passo_a_passo(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                        print("Backtracking...")
                        imprimir_tabuleiro(tabuleiro)
                        time.sleep(0.1)  # Ajuste conforme necessário para a visualização
                return False
    return True

pasta_sudoku = "sudoku_exemplos"
arquivos_sudoku = os.listdir(pasta_sudoku)

while True:
    print("\nMenu:")
    print("1. Selecionar um Sudoku específico")
    print("2. Escolher um Sudoku aleatoriamente")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\nSudoku disponíveis:")
        for i, arquivo in enumerate(arquivos_sudoku):
            print(f"{i + 1}. {arquivo}")

        escolha_arquivo = int(input("Escolha o número do arquivo Sudoku: ")) - 1

        if 0 <= escolha_arquivo < len(arquivos_sudoku):
            caminho_arquivo = os.path.join(pasta_sudoku, arquivos_sudoku[escolha_arquivo])
            tabuleiro_sudoku = ler_sudoku_de_arquivo(caminho_arquivo)

            print(f"Tabuleiro do arquivo '{arquivos_sudoku[escolha_arquivo]}':")
            imprimir_tabuleiro(tabuleiro_sudoku)

            if tabuleiro_valido(tabuleiro_sudoku):
                tempo_inicio = time.time()

                if resolver_sudoku_com_passo_a_passo(tabuleiro_sudoku):
                    tempo_fim = time.time()
                    print("\nSolução encontrada:")
                    imprimir_tabuleiro(tabuleiro_sudoku)
                    tempo_decorrido = tempo_fim - tempo_inicio
                    print(f"\nTempo decorrido: {tempo_decorrido:.5f} segundos")

                    if esta_correto(tabuleiro_sudoku):
                        print("O Sudoku foi resolvido corretamente!")
                    else:
                        print("O Sudoku foi resolvido, mas não está correto.")
                else:
                    print("\nNão há solução para o tabuleiro fornecido.")
            else:
                print("O tabuleiro fornecido não é válido.")
        else:
            print("Número de arquivo Sudoku inválido.")

    elif escolha == "2":
        arquivo_aleatorio = random.choice(arquivos_sudoku)
        caminho_arquivo = os.path.join(pasta_sudoku, arquivo_aleatorio)

        tabuleiro_sudoku = ler_sudoku_de_arquivo(caminho_arquivo)

        print(f"Tabuleiro do arquivo '{arquivo_aleatorio}':")
        imprimir_tabuleiro(tabuleiro_sudoku)

        if tabuleiro_valido(tabuleiro_sudoku):
            tempo_inicio = time.time()

            if resolver_sudoku_com_passo_a_passo(tabuleiro_sudoku):
                tempo_fim = time.time()
                print("\nSolução encontrada:")
                imprimir_tabuleiro(tabuleiro_sudoku)
                tempo_decorrido = tempo_fim - tempo_inicio
                print(f"\nTempo decorrido: {tempo_decorrido:.5f} segundos")

                if esta_correto(tabuleiro_sudoku):
                    print("O Sudoku foi resolvido corretamente!")
                else:
                    print("O Sudoku foi resolvido, mas não está correto.")
            else:
                print("\nNão há solução para o tabuleiro fornecido.")
        else:
            print("O tabuleiro fornecido não é válido.")

    elif escolha == "3":
        break

    else:
        print("Opção inválida. Escolha novamente.")
