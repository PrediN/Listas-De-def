# 10: Crie uma função que receba uma lista de números e retorne essa lista ordenada em ordem crescente.

# Declaração de variaveis

listaNumeros = [2, 8, 4, 5, 10, 3, 1, 6, 9, 7]

# Declaração de função

def organizador(lista):
    lista.sort()
    print(lista)

# Chamada da função

print(listaNumeros)
organizador(listaNumeros)