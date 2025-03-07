# 3. Crie uma função que recebe uma lista de números e retorna a quantidade de números que são múltiplos de 3.

# Declaração de variaveis

lista = [1, 2, 7, 8, 9, 10, -3, -2, -4, -1]

# Declaração de função

def multiplos(listaNum, contador = 0):
    for i in listaNum:
        if i % 3 == 0:
            contador +=1
    return f"A quantidade de números múltiplos de 3 é {contador}"

# Apresentação de resultados

print(multiplos(lista))