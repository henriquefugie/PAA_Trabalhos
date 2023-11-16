import random

def encontrar_maior_subarray(arr, baixo, alto):
    # Caso base: subarray com um único elemento
    if baixo == alto:
        return baixo, alto, arr[baixo]

    # Encontrar índice do meio
    meio = (baixo + alto) // 2

    # Encontrar a soma máxima do subarray na parte esquerda
    esquerda_baixo, esquerda_alto, soma_max_esquerda = encontrar_maior_subarray(arr, baixo, meio)

    # Encontrar a soma máxima do subarray na parte direita
    direita_baixo, direita_alto, soma_max_direita = encontrar_maior_subarray(arr, meio + 1, alto)

    # Encontrar a soma máxima que cruza o meio
    cruzando_baixo, cruzando_alto, soma_max_cruzando = encontrar_soma_maxima_cruzando(arr, baixo, meio, alto)

    # Retornar o subarray com a maior soma entre as três
    if soma_max_esquerda >= soma_max_direita and soma_max_esquerda >= soma_max_cruzando:
        return esquerda_baixo, esquerda_alto, soma_max_esquerda
    elif soma_max_direita >= soma_max_esquerda and soma_max_direita >= soma_max_cruzando:
        return direita_baixo, direita_alto, soma_max_direita
    else:
        return cruzando_baixo, cruzando_alto, soma_max_cruzando


def encontrar_soma_maxima_cruzando(arr, baixo, meio, alto):
    # Encontrar a soma máxima à esquerda do meio
    soma_max_esquerda = float('-inf')
    soma_atual = 0
    esquerda_baixo = meio
    for i in range(meio, baixo - 1, -1):
        soma_atual += arr[i]
        if soma_atual > soma_max_esquerda:
            soma_max_esquerda = soma_atual
            esquerda_baixo = i

    # Encontrar a soma máxima à direita do meio
    soma_max_direita = float('-inf')
    soma_atual = 0
    direita_alto = meio + 1
    for i in range(meio + 1, alto + 1):
        soma_atual += arr[i]
        if soma_atual > soma_max_direita:
            soma_max_direita = soma_atual
            direita_alto = i

    # Retornar o subarray que cruza o meio
    return esquerda_baixo, direita_alto, soma_max_esquerda + soma_max_direita


# Função para gerar um array aleatório
def gerar_array_aleatorio(tamanho):
    return [random.randint(-100, 100) for _ in range(tamanho)]

# Exemplo de uso
escolha_usuario = input("Deseja fornecer um array manualmente? (S/N): ").upper()

if escolha_usuario == 'S':
    array_usuario = list(map(int, input("Digite os elementos do array separados por espaço: ").split()))
else:
    tamanho_array = random.randint(1, 10)
    array_usuario = gerar_array_aleatorio(tamanho_array)

print("Array fornecido:", array_usuario)

tamanho_array = len(array_usuario)
baixo, alto, maior_subarray_soma = encontrar_maior_subarray(array_usuario, 0, tamanho_array - 1)

print(f"O maior subarray contíguo possui soma: {maior_subarray_soma}")
print(f"Subarray usado: {array_usuario[baixo:alto+1]}")