#Trabalho 2 PAA
#trabalho apresentado

# Este código em comparacão ao primeiro ficou bem menor,
# mas possui uma estrutura similar, onde primeiro ele resolve o problema e em seguida
# tem o código que cuida do MENU do programa

# Para solucionar o problema da Torre de Hanoi, foi utilizado chamada recursiva que ocorre mais a frente no código
def resolver_torre_de_hanoi(n, origem, auxiliar, destino):
    
    # Nesta primeira etapa nos temos o caso base da recursão, que é quando n é igual 1, ou seja, temos apenas 1 disco para ser movido e para solucionar este caso base,
    # o disco 1 é movido da origem até o destino, através das funcoes append e pop, pois foi utilizado lista e para adicionar o elemento no final da lista e remover 
    # do final da lista tambem, sao utilizadas esta funcoes.
    
    # print(f"Resolvendo torre de Hanoi para {n} discos de {origem} para {destino} usando {auxiliar} como auxiliar.")
    
    if n == 1:
        print(f"mover o disco 1 de {origem} para {destino}")
        pinos[destino].append(pinos[origem].pop())
        print_estado_pinos()
        return True
    
    # Agora é onde a recursão/Inducão ocorre, neste parte do código temos duas chamadas recursivas, mais conhecida como inducão recursiva
    # onde após a chamada da funcao para resolver o problema, digamos como exemplo, uma entrada com 3 discos, primeiro ele faz a verificacão no caso base (n == 1)
    # e caso ela não seja satisfeita, ela faz uma chamada recursiva, alternando as posicoes de destino e auxiliar
    
    # O codigo funciona da seguinte forma, ela passa pelo caso base, e caso seja falso, ou seja, possui mais de um disco, ele faz uma divisão de subproblemas em problemas menores
    # executando uma chamada recursiva movendo todos os discos, execeto o maior da origem para o auxiliar, usando o destino como "auxiliar" e em seguida é feita uma segunda
    # chamada recursiva que movimenta os discos menores da torre dos auxiliares para a torre de destino usando a origem como "auxiliar" e esse processo se repete até que todos
    # os discos estejam na torre destino
     
    if resolver_torre_de_hanoi(n - 1, origem, destino, auxiliar):
        # print(f"Resolvendo1 torre de Hanoi para {n} discos de {origem} para {destino} usando {auxiliar} como auxiliar.")
        print(f"mover o disco {n} de {origem} para {destino}")
        pinos[destino].append(pinos[origem].pop())
        print_estado_pinos()
        
        if resolver_torre_de_hanoi(n - 1, auxiliar, origem, destino):
            return True
    return False

# Uma simples funcao que percorre os itens do dicionário de pinos e mostra o conteúdo de cada item, sendo eles, origem, auxiliar e destino
def print_estado_pinos():
    print("Estado dos pinos:")
    for pino, discos in pinos.items():
        print(f"{pino}: {discos}")
    print()

# Solicitar o número de discos
n = int(input("Digite o número de discos: "))

# Solicitar os nomes dos pinos
origem = input("Digite o nome do pino de origem: ")
auxiliar = input("Digite o nome do pino auxiliar: ")
destino = input("Digite o nome do pino de destino: ")

# Os pinos da Torre de Hanoi foram definidos em um dicionário, onde a posicao origem possui uma lista que comeca do número n, fornecido pelo usuário e vai até 
# o número 1 em ordem descrescente, representando uma pilha, pois os números maiores estão do lado esquerdo da lista e os menores do lado direito
pinos = {
    origem: list(range(n, 0, -1)),
    auxiliar: [],
    destino: []
}

# Aqui ocorre a chamada da funcao para resolver o problema com as variaveis em seus devidos lugares e fornecidas pelo usuário corretamente
print_estado_pinos()
if not resolver_torre_de_hanoi(n, origem, auxiliar, destino):
    print("Não foi possível encontrar uma solução.")