# 6. Crie uma função que recebe uma lista de palavras e retorna a palavra com mais letras.

# Declaração de variaveis

palavras = ["banana", "maçã", "laranja", "abacaxi"]

# Declaração de função

def maiorPalavra(lista):
    return max(lista, key=len)

# Apresentação de resultados

print(maiorPalavra(palavras))