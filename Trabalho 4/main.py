#Trabalho 4 PAA

def menor_tamanho_subsequencia(a, b):
    #Inicio da funcao principal do código, que faz a geracao da tabela dp e faz  o preenchimento da mesma, utilizando valores anteriores para continuar a solucao.
    # funcao simples para adquirir o tamanho das strings e gerar a matriz do taamnho que as astrings possuem mais 1, para garantir que nos casos mais simples e base,
    # ele nao de problema na transferencia de dados dos subproblemas
    tam_a = len(a)
    tam_b = len(b)

    matriz = [[0] * (tam_b + 1) for _ in range(tam_a + 1)]

    # Neste loops aninhados ele percorre as duas palavras, de forma a comparar todos os caracteres que as strings possuem, com +1 pois o for é exclusivo
    for i in range(1, tam_a + 1):
        for j in range(1, tam_b + 1):
            # Esta verificacao que identifica se as letras que estao sendo analisadas sao iguais ou nao, e caso nao sejam, ele executa um preenchimento diferente.
            if a[i - 1] == b[j - 1]:
                
                # Neste parte, caso as letras sejam iguais, ele pega o resultado anterior, na posicao diagonal, onde foi analisado outras letras, na posicao anterior com certeza
                # e soma mais 1, para que o valor que esta sendo carregado pela tabela dp seja correto em relacao as letras iguais, por isso a cada letra igua lque ele achar ele vai somar mais 1
                
                matriz[i][j] = matriz[i - 1][j - 1] + 1
            else:
                
                # Neste caso, onde as letras analisadas nao sao iguais, ele se utiliza de resultados anteriores, para definir o valor na celula da tabela dp, onde ele pega o maior valor
                # da analise entre as letras da celula anterior, ou na celula da mesma coluna, no ponto acima que ja foi preenchido, e o que for maior, ele vai passar adiante.
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])

    # Neste final, ele pega o resultado que chegou na ultima casa da tabela dp, que possui o valor da quantdiade total de letras que se repetem, entao, é simples agora para
    # encontrar o valor de letras que nao se repetem, é necessario apenas somar a quantidade de letras da primeira string com a segunda e reomver a quantidade de letras que se
    # repetem de uma das strings, que é o que esta sendo feito aqui, chegando assim no resultado final
    
    menor_tamanho = tam_a + tam_b - matriz[tam_a][tam_b]
    return menor_tamanho

# Entrada
string_a = input().strip()
string_b = input().strip()

# Saída
print(menor_tamanho_subsequencia(string_a, string_b))
