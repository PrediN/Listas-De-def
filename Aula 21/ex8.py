# 8: Crie uma função que receba uma lista de notas e retorne a média das notas.

# Declaração de variaveis

notas = [7.5, 9.0, 6.2, 8.8]

# Declaração de função

def media(lista, soma = 0, contador = 0):
    for i in lista:
        soma += i
        contador += 1
    mediaFinal = soma/contador
    return mediaFinal

# Apresentação de resultados

print(f"{media(notas):.2f}")