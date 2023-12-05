# Este código foi o mesmo utilizado no beecrowd, então alguns pontos como, retorno de funcoes e entradas foram alteradas para que seja aceito no beecrowd

def maior_premio(n, d, numero):
    
    # A funcao maior_premio comeca inciando uma pilha, apenas para manipular de forma correta e precisa o numero, sem que algum numero saia do local
    pilha = []

    # É feito um loop de digito em volta do número, percorrendo todos os números enviador pelo usuário
    for digito in numero:
        
        # Enquanto ainda precisamos remover dígitos, há elementos na pilha e o último elemento é menor que o digito atual, ele vai remover o número que esta na pilha
        # que é menor que o digito que ele esta para preencher e colocar e vai removendo até que a pilha fique vazia/ o numero seja maior que o digito/o numero de digitos
        # que precisa ser removido seja igual a 0
        
        while d > 0 and pilha and pilha[-1] < digito:
            pilha.pop() # Aqui ele remove o ultimo numero da pilha que é menor que o digito
            d -= 1 # Aqui ele vai decrementando o valor de d que é a quantidade de numeros que precisa ser removida
        pilha.append(digito) # Toda vez que um laco do for, for executado um numero sera adicionado pelo append

    # Se ainda houver dígitos a serem removidos, remova do final, isso é mais para previnir erros, para garantir que o resultado seja correto.
    pilha = pilha[:-d] if d > 0 else pilha

    # Junte os dígitos para formar o maior prêmio como uma string e retorna para a main
    resultado = ''.join(pilha)

    return resultado

def main():
    
    # Foi feito um laco de repeticao que detecta se a entrada foi 0 0 que deveria finalizar o programa, caso contrario ele executa o que foi pedido
    while True:
        
        # Aqui ele recebe um map de ints que é separado, pois a entrada no beecrowd deve ser (4 2) e depois um número que é lido com numero logo abaixo
        n, d = map(int, input().split())
        if n == 0 and d == 0:
            break

        numero = input().strip()
        
        # Por fim aqui ele chama a funcao principal do código e printa o resultado que é o número do premio de maior valor
        resultado = maior_premio(n, d, numero)
        print(resultado)

if __name__ == "__main__":
    main()
