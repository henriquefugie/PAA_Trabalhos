#Trabalho 1 PAA
#trabalho apresentado

import os       #listar os sudokus da pasta sudoku_exemplos
import random       #Escolher aleatoriamente um dos sudokus da pasta
import time 	    #Calcular o tempo que o solver demora para solucionar o sudoku

#Funcao utilizada para printar o tabuleiro iterando cada linha do tabuleiro, convertendo os numeros em string, separando eles por " " e printando a linha
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))

#Esta funcao verifica se o tabuleiro que esta sendo gerado é um tabuleiro válido ou não, se não possui algum numero repetido na linha. na coluna e no quadrante
def tabuleiro_valido(tabuleiro):
    #verifica as linhas
    for linha in tabuleiro:
        linha_set = set()
        # Cria um conjunto vazio para armazenar os números na linha
        for num in linha:
            if num != 0 and num in linha_set:
                return False
            linha_set.add(num)
            #Apos ele verificar, se o numero é diferente de zero e se ele nao apareceu na linha ainda, ele vai adicionar no set e continuar verificando a linha
            
    #verifica as colunas
    for coluna in range(9):
        coluna_set = set()
        # Cria um conjunto vazio para armazenar os números na coluna
        for linha in range(9):
            num = tabuleiro[linha][coluna]
            if num != 0 and num in coluna_set:
                return False
            coluna_set.add(num)
            #Apos ele verificar, se o numero é diferente de zero e se ele nao apareceu na coluna ainda, ele vai adicionar no set e continuar verificando a coluna
            
    #verifica os quadrantes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrante_set = set()
            # Cria um conjunto vazio para armazenar os números no quadrante
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    num = tabuleiro[x][y]
                    if num != 0 and num in quadrante_set:
                        return False
                    quadrante_set.add(num)
                    #Apos ele verificar, se o numero é diferente de zero e se ele nao apareceu no quadrante ainda, ele vai adicionar no set e continuar verificando o quadrante
                    
    return True
    #Caso o tabuleiro seja valido ele retorna True e comeca a resolver o tabuleiro
    
#Esta funcao tambem faz uma verificacao parecida com a de cima, porém faz a verificacao durante o preenchimento do tabuleiro, ele que verifica a casa que o solver vai preencher
def validade(tabuleiro, linha, coluna, num):
    
    #Atrvés deste laco de repeticao ele verifica as linhas e colunas, comparando o numero na posicao com o numero que vai ser preenchido, verificando se ja nao foi preenchido
    for i in range(9):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False

    #Esta operacao serve para encontrar em qual quadrante a verificacao esta, sendo 3 quadrantes 0(0,2) 1(3, 5) 2(6, 8)
    #A divisao //3 retorna o maior numero inteiro
    inicio_linha, inicio_coluna = 3 * (linha // 3), 3 * (coluna // 3)
    
    #Depois de pegar a posicao inicial do quadrante, ele percorre o 3x3 do quadrante verificando o num se ja existe, se nao existe, ele retorna True
    for i in range(3):
        for j in range(3):
            if tabuleiro[inicio_linha + i][inicio_coluna + j] == num:
                return False
    return True

#Esta é a funcao mais importante do código que resolve o sudoku através do paradigma de forca bruta backtracking
def resolver_sudoku(tabuleiro):
    #Primeiramente ele vai percorrer o tabuleiro inteiro verificando se a celular  possui o valor 0 (nos mapas de sudoku fornecidos são as celulas não preenchidas)
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                #Aqui ele passa por todos os números disponíveis que podem ser colocados em uma célula (1 a 9) e faz a verificacao com a funcao validade se o número pode ser colocado, se sim, ele atribui na célula
                for num in range(1, 10):
                    if validade(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        #Neste ponto o backtracking atua, chamando de forma recursiva a funcao para tentar resolver o restante do sudoku
                        if resolver_sudoku(tabuleiro):
                            return True
                        # Backtracking: caso ele nao leve a uma solucao válida, ele desfaz a atribuicao da celula
                        tabuleiro[linha][coluna] = 0
                #Retorna false se nenhum numero valido puder ser atribuido na celula
                return False
    #Se o tabuleiro for totalmente preenchido de forma correta, retorna True
    return True

#Segunda verificacao sugerida onde ele verifica se a soma das linhas/colunas/quadrantes é igual a 45
def esta_correto(tabuleiro):
    # Verifica a soma das linhas e colunas
    for i in range(9):
        #Utilizando sum, ele soma os valores contidos na linha inteira e na coluna inteira, e verifica se as somas são iguais a 45, se for igual a 45 está certo
        soma_linha = sum(tabuleiro[i])
        soma_coluna = sum(tabuleiro[j][i] for j in range(9))
        if soma_linha != 45 or soma_coluna != 45:
            return False

    # Verifica a soma dos quadrantes, utilizando a mesma lógica de percorrer os quadrantes e a da soma dar 45, se fro 45, está correto
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            soma_quadrante = sum(tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3))
            if soma_quadrante != 45:
                return False
    if tabuleiro_valido(tabuleiro):
        return True
    else:
        return False

# Função para ler o Sudoku de um arquivo de texto
def ler_sudoku_de_arquivo(nome_arquivo):
    #Utilizando uma lista, ele armazena outras listas(as linhas do sudoku) que são convetidos em int para as operacoes de verificar os quadrantes funcionar, separando cada numero corretamente
    tabuleiro_sudoku = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha_sudoku = [int(x) for x in linha.split()]
            tabuleiro_sudoku.append(linha_sudoku)
    return tabuleiro_sudoku


#Leitura da pasta sudoku_exemplos para escolher na opcao 1 do menu
pasta_sudoku = "sudoku_exemplos"
arquivos_sudoku = os.listdir(pasta_sudoku)

#MENU do código, não é necessário comentário para explicar, acredito estar bem autoexplicativo
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

            if tabuleiro_valido(tabuleiro_sudoku):      # Verificar a validade
                tempo_inicio = time.time()      # Início da contagem de tempo

                if resolver_sudoku(tabuleiro_sudoku):
                    tempo_fim = time.time()     # Fim da contagem de tempo
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

        if tabuleiro_valido(tabuleiro_sudoku):      #Verificar a validade
            tempo_inicio = time.time()      #Início da contagem de tempo

            if resolver_sudoku(tabuleiro_sudoku):
                tempo_fim = time.time()     #Fim da contagem de tempo
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