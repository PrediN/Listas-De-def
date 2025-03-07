# 5. Crie uma função que recebe uma lista de números e substitui os números negativos por zero.

# Declaração de variaveis

lista = [1, 2, 7, 8, 9, 10, -3, -2, -4, -6.3]

# Declaração de função

def trocarPorZero(listaNum):
    for i in range(len(listaNum)):
        if listaNum[i] <= 0:
            listaNum[i] = 0
    return listaNum

# Apresentação  de resultados

trocarPorZero(lista)
print(lista)