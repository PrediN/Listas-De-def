# 7. Crie uma função que recebe uma lista de números e retorna a soma apenas dos números pares.

# Declaração de variaveis

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Declaração de função

def somaPares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return f"A soma dos números pares é {soma}"

# Apresentação de resultados

print(somaPares(numeros))