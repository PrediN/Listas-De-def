# 2. Crie uma função que recebe uma lista de números e retorna a quantidade de números positivos.

# Declaração de variaveis

lista = [1, 2, 7, 8, 9, 10, -3, -2, -4, -6.3]


# Declaração de função

def positivos(listaNum, contador = 0):
    for i in listaNum:
        if i > 0:
            contador +=1
    return f"A quantidade de números positivos é {contador}"

# Apresentação de resultados

print(positivos(lista))