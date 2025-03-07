# 3: Crie uma função chamada media_lista que recebe uma lista de números e retorna a média deles.

# Delcaração de função

def mediaLista (notas, contador, soma):
    for i in notas:
        contador += 1
        soma += i
    media = soma / contador
    return media

# Declaração de variaveis

listaNotas = [8, 7, 9, 4, 5, 6]
contador = 0
soma = 0

# Apresentação de resultados

print (mediaLista(listaNotas, contador, soma))