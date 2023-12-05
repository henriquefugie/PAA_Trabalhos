#Trabalho 3 PAA
#trabalho apresentado

import random
import math

def cruzada(vetor, inicio, meio, fim):
    
    # A funcao cruzada é responsável por encontrar o array que é equivalente a juncao do array que foi encontrado na esquerda com o que foi encontrado na direita,
    # de forma que ele recebe o valor do meio e vai percorrendo a area da esquerda até encontrar o inicio do array, de forma que caso a adicao da posicao do array nao faca difererenca
    # para a soma da esquerda, ele nao sera adicionado no cruzamento, mesma coisa para a direita, onde ele comeca do meio do vetor, e vai até o final, utilizando a mesma lógica
    # que foi feita para encontrar a parte da esquerda.
    # Um ponto imporante a se destacar é que como a funcao cruzada está no meio das chamadas recursivas, os índices de inicio e fim durante as solucoes de divisoes está correto,
    # pode ser observado no main_debug, os indices vao se adaptando dependendo de qual momento a solucao está, fazendo com que nao seja necessário identificar precisamente a posicao.
    max_esq = max_dir = float('-inf')
    max_atual = 0
    inicio_cruzamento = fim_cruzamento = meio

    # Encontra a maior soma no subvetor à esquerda
    for i in range(meio, inicio - 1, -1):
        max_atual += vetor[i]
        if max_atual > max_esq:
            max_esq = max_atual
            inicio_cruzamento = i

    max_atual = 0

    # Encontra a maior soma no subvetor à direita
    for i in range(meio + 1, fim + 1):
        max_atual += vetor[i]
        if max_atual > max_dir:
            max_dir = max_atual
            fim_cruzamento = i
            
    aux = vetor[inicio_cruzamento:fim_cruzamento + 1]
    return aux

def maiorSubArrayRecursivo(vetor, inicio, fim):
    
    # Esta funcao é a principal do código, onde ele possui primeiramente um caso base, que é quando o inicio é igual ao fim e quando isso acontece, ele vai passa pela esquerda
    # e vai para a segunda chamada recursiva direita.
    # Nesta chamada recursiva da esquerda primeiramente, ela separa o array ao meio e depois separa ao meio denovo, resolvendo um problema menor para ir proseguindo com as demais solucoes,
    # ele vai repetindo esse processo de encontra esquerda, encontra direita, faz o cruzamento até alcancar o objetivo final que é quando o cruzamento recebe o array inteiro, mesmo não fazendo o cruzamento
    # considerando o vetor inteiro.
    if inicio == fim:
        return vetor[inicio:inicio + 1]

    meio = (inicio + fim) // 2
    esquerda = maiorSubArrayRecursivo(vetor, inicio, meio)
    direita = maiorSubArrayRecursivo(vetor, meio + 1, fim)
    cruzamento = cruzada(vetor, inicio, meio, fim)
    cadeia = verifica(esquerda, cruzamento, direita)

    return cadeia

def verifica(esq, meio, direita):
    
    # Esta parte do código que retornar basicamente qual das tres cadeias encontradas, tanto pela esquerda, quando pela direita e pelo meio, qual delas possui o maior valor
    # de soma, e o que for escolhido é retornado, e assim em diante, a cada recursão feita, onde os valores de esquerda, direita e cruzamento foram encontrado
    s1 = sum(esq)
    s2 = sum(direita)
    s3 = sum(meio)

    if s1 >= s2 and s1 >= s3:
        return esq
    elif s2 >= s1 and s2 >= s3:
        return direita
    else:
        return meio

# Este código comeca deste ponto onde ele mostra um menu se o usuario deseja receber um array aleatorio de 10 posicoes, ou digitar um array proprio
print("1. Array Aleatorio")
print("2. Array Digitado")
escolha = input("Escolha uma opção: ")

if escolha == "1":
    array = [random.randint(-100, 100) for _ in range(10)]
elif escolha == "2":
    array_digitado = input("Digite o array - Ex(1,2,3,4,5,6):")
    array = [int(numero) for numero in array_digitado.split(',')]

# O array é mostrado para fins de confirmacao, para garantir que o array foi digitado corretamente
print(array)

# Chama a função recursiva para encontrar a maior soma em subvetores e o -1 é porque o array comeca do 0, ai o len encontra 10, sendo que o array vai até 9
subvetor_max = maiorSubArrayRecursivo(array, 0, len(array) - 1)
soma_max = sum(subvetor_max)

print("A maior soma é {} encontrada na subcadeia {}".format(soma_max, subvetor_max))
