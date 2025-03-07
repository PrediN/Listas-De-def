# 7: Crie uma função que receba uma lista de números e retorne o maior número dessa lista.

# Declaração de função

def maiorNum(listaNum):
    maior = listaNum[0]
    for num in listaNum:
        if num > maior:
            maior = num
    return maior

# Declaração de variveis

lista = [37, 82, 12, 95, 5, 68, 23, 79, 41, 56]

# Apresentação de resultados

print(maiorNum(lista))