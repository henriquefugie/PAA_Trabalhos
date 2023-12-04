def maior_premio(n, d, numero):
    pilha = []

    for digito in numero:
        print(pilha)
        # Enquanto ainda precisamos remover dígitos, há elementos na pilha e o último elemento é menor que o digito atual
        print()
        while d > 0 and pilha and pilha[-1] < digito:
            pilha.pop()
            d -= 1
        pilha.append(digito)

    # Se ainda houver dígitos a serem removidos, remova do final
    pilha = pilha[:-d] if d > 0 else pilha
    print(pilha)

    # Junte os dígitos para formar o maior prêmio como uma string
    resultado = ''.join(pilha)

    return resultado

def main():
    while True:
        n, d = map(int, input().split())
        if n == 0 and d == 0:
            break

        numero = input().strip()
        resultado = maior_premio(n, d, numero)
        print(resultado)

if __name__ == "__main__":
    main()
