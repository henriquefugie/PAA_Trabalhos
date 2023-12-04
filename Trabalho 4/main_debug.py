def print_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def menor_tamanho_subsequencia(a, b):
    tam_a = len(a)
    tam_b = len(b)

    matriz = [[0] * (tam_b + 1) for _ in range(tam_a + 1)]
    print("Matriz inicial gerada: \n")
    print_matriz(matriz)
    print("\n")

    for i in range(1, tam_a + 1):
        for j in range(1, tam_b + 1):
            print(f"Comparando {a[i - 1]} da primeira palavra com {b[j - 1]} da segunda palavra\n")
            if a[i - 1] == b[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + 1
                print(f"Encontrou que {a[i - 1]} e igual a {b[j - 1]}")
                print(f"Paga o valor na posicao {i-1}x{j-1} = {matriz[i - 1][j - 1]} e soma 1, ficando {matriz[i][j]} na posicao {i}x{j}\n")
                print_matriz(matriz)
                print("\n")
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])
                print_matriz(matriz)
                print("\n")

    print_matriz(matriz)
    print("\n")
    print(f"Na posicao {tam_a} x {tam_b} da matriz, a quantidade de letras que foram iguais foi: {matriz[tam_a][tam_b]}\n")
    menor_tamanho = tam_a + tam_b - matriz[tam_a][tam_b]
    return menor_tamanho

# Entrada
string_a = input().strip()
string_b = input().strip()

# Saída
print(menor_tamanho_subsequencia(string_a, string_b))