def cruzada(vetor, inicio, meio, fim):
    max_esq = -999999
    max_atual = 0
    inicio_cruzamento = meio
    fim_cruzamento = meio

    for i in range(meio, inicio - 1, -1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_esq:
            max_esq = max_atual
            inicio_cruzamento = i

    max_dir = -999999
    max_atual = 0

    for i in range(meio + 1, fim + 1):
        max_atual = max_atual + vetor[i]
        if max_atual > max_dir:
            max_dir = max_atual
            fim_cruzamento = i
            
    aux = array[inicio_cruzamento:fim_cruzamento+1]
    return aux


def maiorSubArray(a, inicio, fim):
    max_atual = max_global = 0
    aux = []
    i1 = i2 = f1 = f2 = 0
    ig1 = ig2 = fg1 = fg2 = 0


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

    aux = a[ig1:fg1+1]
    return aux

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

    if (s1 > s2) and (s1 > s3):
        return s1, esq
    if (s2 > s1) and (s2 > s3):
        return s2, direita
    if (s3 > s1) and (s3 > s2):
        return s3, meio

array = [-2, -3, 4, -1, -2, 1, 5, -3]
meio = int(len(array)/2)
if(len(array)%2 == 0):
    meio = int(len(array)/2) - 1
esquerda = maiorSubArray(array, 0, meio)
direita = maiorSubArray(array, meio, len(array))
cruzamento = cruzada(array, 0, meio, len(array) - 1)
soma, cadeia = verifica(esquerda,cruzamento,direita)
print("A maior soma é {} encontrada na subcadeia {}".format(soma, cadeia))
