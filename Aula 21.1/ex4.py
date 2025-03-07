# 4. Crie uma função que recebe uma lista de palavras e junta tudo em uma única frase.

# Declaração de variaveis

frase = ["O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma"]

# Declaração de função

def montarFrase (lista):
    for i in lista:
        print(i, end=" ")

# Apresentação de resultados

montarFrase(frase)

print()