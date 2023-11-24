import random
import math

def cruzada(vetor, inicio, meio, fim):
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
    if inicio == fim:
        return vetor[inicio:inicio + 1]

    meio = (inicio + fim) // 2
    esquerda = maiorSubArrayRecursivo(vetor, inicio, meio)
    direita = maiorSubArrayRecursivo(vetor, meio + 1, fim)
    cruzamento = cruzada(vetor, inicio, meio, fim)
    soma, cadeia = verifica(esquerda, cruzamento, direita)

    return cadeia

def verifica(esq, meio, direita):
    s1 = sum(esq)
    s2 = sum(direita)
    s3 = sum(meio)

    if s1 >= s2 and s1 >= s3:
        return s1, esq
    elif s2 >= s1 and s2 >= s3:
        return s2, direita
    else:
        return s3, meio

print("1. Array Aleatorio")
print("2. Array Digitado")
escolha = input("Escolha uma opção: ")

if escolha == "1":
    array = [random.randint(-100, 100) for _ in range(10)]
elif escolha == "2":
    array_digitado = input("Digite o array: ")
    array = [int(numero) for numero in array_digitado.split(',')]

print(array)

# Chama a função recursiva para encontrar a maior soma em subvetores
subvetor_max = maiorSubArrayRecursivo(array, 0, len(array) - 1)
soma_max = sum(subvetor_max)

print("A maior soma é {} encontrada na subcadeia {}".format(soma_max, subvetor_max))
