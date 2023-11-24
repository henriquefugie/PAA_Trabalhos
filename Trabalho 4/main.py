def menor_tamanho_subsequencia(a, b):
    tam_a = len(a)
    tam_b = len(b)

    matriz = [[0] * (tam_b + 1) for _ in range(tam_a + 1)]

    for i in range(1, tam_a + 1):
        for j in range(1, tam_b + 1):
            if a[i - 1] == b[j - 1]:
                matriz[i][j] = matriz[i - 1][j - 1] + 1
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])

    menor_tamanho = tam_a + tam_b - matriz[tam_a][tam_b]
    return menor_tamanho

# Entrada
string_a = input().strip()
string_b = input().strip()

# Saída
print(menor_tamanho_subsequencia(string_a, string_b))
