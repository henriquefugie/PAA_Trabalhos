import random

def cruzada(vetor, inicio, meio, fim):
    max_esq = max_dir = float('-inf')
    max_atual = 0
    inicio_cruzamento = fim_cruzamento = meio

    for i in range(meio, inicio - 1, -1):
        max_atual += vetor[i]
        if max_atual > max_esq:
            max_esq = max_atual
            inicio_cruzamento = i

    max_atual = 0

    for i in range(meio + 1, fim + 1):
        max_atual += vetor[i]
        if max_atual > max_dir:
            max_dir = max_atual
            fim_cruzamento = i
            
    return vetor[inicio_cruzamento:fim_cruzamento + 1]

def maiorSubArrayRecursivo(vetor, inicio, fim):
    if inicio == fim:
        return [vetor[inicio]]  # Retorna uma lista com um único elemento

    meio = (inicio + fim) // 2

    print(f"Chamando recursivamente com vetor[{inicio}:{meio}]")
    esquerda = maiorSubArrayRecursivo(vetor, inicio, meio)

    print(f"Chamando recursivamente com vetor[{meio+1}:{fim}]")
    direita = maiorSubArrayRecursivo(vetor, meio + 1, fim)

    print(f"Chamando cruzada com vetor[{inicio}:{meio}:{fim}]")
    cruzamento = cruzada(vetor, inicio, meio, fim)

    print(f"Verificando subvetores: {esquerda}, {cruzamento}, {direita}")
    return verifica(esquerda, cruzamento, direita)

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

# Geração do array aleatório
array = [random.randint(-100, 100) for _ in range(10)]

print("Array:", array)

# Chama a função recursiva para encontrar a maior soma em subvetores
resultado = maiorSubArrayRecursivo(array, 0, len(array) - 1)
soma_max, subvetor_max = resultado

print(f"A maior soma é {soma_max} encontrada na subcadeia {subvetor_max}")
