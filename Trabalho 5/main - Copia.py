def junta_string(arr):
    aux = ""
    for i in arr:
        aux = aux + str(i)
    aux = int(aux)
    return aux

def p1084(n, d, arr, cont):
    if(n == d):
        arr = junta_string(arr)
        return arr
    elif cont == len(arr):
        print("Impossível, pois a quantidade de números que vão ser apagados é maior do que a quantidade de números")
    else:
        while(cont != 0):
            for i in arr:
                aux = min(arr)
                arr.remove(aux)
                cont = cont - 1
                break
        arr = junta_string(arr)
        return arr
        


n = int(input("Digite a quantidade de números que foram escritos: "))
d = int(input("Digite quantos números devem ser apagados: "))
num = int(input("Digite o número que vai ser analisado: "))
aux = str(num)
arr = []
for i in aux:
    arr.append(int(i))   
print("O Número Original digitado foi: {}".format(aux)) 
res = p1084(n, d, arr, d)
print("A resposta é: {}".format(res))
