def maior_premio(n, d, numero):
    pilha = []

    for digito in numero:
        while d > 0 and pilha and pilha[-1] < digito:
            print(f"O digito {digito} é maior que {pilha[-1]} que sera removido\n")
            pilha.pop()
            print(f"Pilha apos a remocao do ultimo digito que ela possuia {pilha}\n")
            d -= 1
        pilha.append(digito)
        print(f"Visualizacao da pilha apos adicionar um novo digito {pilha}\n")
        
    print(f"Visualizacao da pilha antes de remover os {d} que faltaram ser removidos {pilha}\n")
    pilha = pilha[:-d] if d > 0 else pilha
    print(f"Visualizacao da pilha final {pilha}\n")
    
    resultado = ''.join(pilha)

    return resultado

def main():
    while True:
        n, d = map(int, input().split())
        if n == 0 and d == 0:
            print(f"Entrada que finaliza o programa encontrada")
            break

        numero = input().strip()
        resultado = maior_premio(n, d, numero)
        print(resultado)

if __name__ == "__main__":
    main()
