def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_de_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_de_hanoi(n - 1, auxiliar, destino, origem)

def resolver_torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print_estado_pinos()
        print(f"Mova o disco 1 de {origem} para {destino}")
        pinos[destino].append(pinos[origem].pop())
        print_estado_pinos()
        return True
    if resolver_torre_de_hanoi(n - 1, origem, auxiliar, destino):
        print_estado_pinos()
        print(f"Mova o disco {n} de {origem} para {destino}")
        pinos[destino].append(pinos[origem].pop())
        print_estado_pinos()
        if resolver_torre_de_hanoi(n - 1, auxiliar, destino, origem):
            return True
    return False

def print_estado_pinos():
    print("Estado dos pinos:")
    for pino, discos in pinos.items():
        print(f"{pino}: {discos}")
    print()

n = int(input("Digite o número de discos: "))
pinos = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}
print_estado_pinos()
if not resolver_torre_de_hanoi(n, 'A', 'C', 'B'):
    print("Não foi possível encontrar uma solução.")
