import random

def cruzada(vetor, inicio, meio, fim):
    max_esq = -999999  # Inicializa a maior soma do subvetor à esquerda com um valor muito baixo
    max_atual = 0     # Inicializa a soma atual
    inicio_cruzamento = meio  # Inicializa o índice de início do subvetor cruzado
    fim_cruzamento = meio    # Inicializa o índice de fim do subvetor cruzado

    # Encontra a maior soma no subvetor à esquerda
    for i in range(meio, inicio - 1, -1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_esq:
            max_esq = max_atual
            inicio_cruzamento = i

    max_dir = -999999  # Inicializa a maior soma do subvetor à direita com um valor muito baixo
    max_atual = 0     # Reinicializa a soma atual

    # Encontra a maior soma no subvetor à direita
    for i in range(meio + 1, fim + 1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_dir:
            max_dir = max_atual
            fim_cruzamento = i
            
    aux = vetor[inicio_cruzamento:fim_cruzamento+1]  # Captura o subvetor com a maior soma cruzada
    return aux


def maiorSubArray(a, inicio, fim):
    max_atual = max_global = 0
    aux = []
    i1 = i2 = f1 = f2 = inicio
    ig1 = ig2 = fg1 = fg2 = inicio

    # Encontra a maior soma do subvetor
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

    aux = a[ig1:fg1+1]  # Captura o subvetor com a maior soma
    return aux, ig1, fg1

def verifica(esq, meio, direita):
    s1 = 0
    s2 = 0
    s3 = 0

    # Calcula a soma dos subvetores esquerdo, cruzado e direito
    for i in range(len(esq)):
        s1 = s1 + esq[i] 
    for i in range(len(direita)):
        s2 = s2 + direita[i]
    for i in range(len(meio)):
        s3 = s3 + meio[i]  

    # Compara as somas e retorna a maior soma e o subvetor correspondente
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

#array = [96, 37, -90, 36, 97, 41, -38, -69, -82, -4]
array = [random.randint(-100, 100) for _ in range(10)]
print(array)
meio = int(len(array)/2)
if(len(array)%2 == 0):
    meio = int(len(array)/2) - 1

# Chama as funções para encontrar a maior soma em subvetores
esquerda, e1, ef1 = maiorSubArray(array, 0, meio)
direita, d1, df1 = maiorSubArray(array, meio, len(array))
cruzamento = cruzada(array, e1, meio, df1)

# Chama a função de verificação para encontrar a maior soma global e o subvetor correspondente
soma, cadeia = verifica(esquerda, cruzamento, direita)
print("Maior subcadeia pela esquerda: {}".format(esquerda))
print("Maior subcadeia pela direita: {}".format(direita))
print("Maior subcadeia pelo cruzamento: {}".format(cruzamento))
print("A maior soma é {} encontrada na subcadeia {}".format(soma, cadeia))
