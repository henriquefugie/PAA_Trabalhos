import random
import math

#https://www.baeldung.com/cs/non-recursive-merge-sort exemplo interativo do mergesort
#fazer com recursão
def cruzada(vetor, inicio, meio, fim):
    max_esq = 0
    max_atual = 0
    inicio_cruzamento = meio
    fim_cruzamento = meio

    for i in range(meio, inicio - 1, -1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_esq:
            max_esq = max_atual
            inicio_cruzamento = i

    max_dir = 0
    max_atual = 0

    for i in range(meio + 1, fim + 1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_dir:
            max_dir = max_atual
            fim_cruzamento = i
            
    aux = vetor[inicio_cruzamento:fim_cruzamento + 1]
    
    print(f"Subvetor à esquerda: {vetor[inicio:meio + 1]}")
    print(f"Subvetor à direita: {vetor[meio + 1:fim + 1]}")
    print(f"Subvetor cruzado: {aux}")
    return aux

def maiorSubArray(a, inicio, fim):
    max_atual = max_global = 0
    aux = []
    i1 = i2 = f1 = f2 = inicio
    ig1 = ig2 = fg1 = fg2 = inicio

    for i in range(inicio, fim):
        if a[i] > max_atual + a[i]:
            max_atual =  a[i]
            i1 = i
            f1 = i
        else:
            max_atual = max_atual + a[i]
            f1 = i

        if max_atual > max_global:
            max_global = max_atual
            ig1 = i1
            fg1 = f1

    aux = a[ig1:fg1 + 1]
    print(f"Subvetor atual: {a[inicio:fim]}")
    print(f"Subvetor com a maior soma: {aux}")
    print("\n")
    return aux, ig1, fg1

def verifica(esq, meio, direita):
    s1 = 0
    s2 = 0
    s3 = 0

    for i in range(len(esq)):
        s1 = s1 + esq[i] 
    for i in range(len(direita)):
        s2 = s2 + direita[i]
    for i in range(len(meio)):
        s3 = s3 + meio[i]  

    print(f"Soma do subvetor à esquerda: {s1}")
    print(f"Soma do subvetor à direita: {s2}")
    print(f"Soma do subvetor cruzado: {s3}")
    print("\n")

    if (s1 > s2) and (s1 > s3):
        return s1, esq
    if (s2 > s1) and (s2 > s3):
        return s2, direita
    if (s3 > s1) and (s3 > s2):
        return s3, meio
    aux = []
    aux.append(s1)
    aux.append(s2)
    aux.append(s3)
    maior = aux.index(max(aux))
    if maior == 0:
        return s1, esq
    elif maior == 1:
        return s2, direita
    return s3, meio

print("1. Array Aleatorio")
print("2. Array Digitado")
escolha = input("Escolha uma opção: ")
print("\n")

if escolha == "1":
    array = [random.randint(-100, 100) for _ in range(10)]
elif escolha == "2":
    array_digitado = input("Digite o array: ")
    print("\n")
    array = [int(numero) for numero in array_digitado.split(',')]

print(f"Array: {array}")
print("\n")
print(len(array))
meio = math.ceil(len(array) / 2)
print(f"Valor de meio {meio}")

esquerda, e1, ef1 = maiorSubArray(array, 0, meio)
direita, d1, df1 = maiorSubArray(array, meio, len(array))
cruzamento = cruzada(array, e1, meio - 1, df1)
soma, cadeia = verifica(esquerda, cruzamento, direita)

print(f"A maior soma é {soma} encontrada na subcadeia {cadeia}")
