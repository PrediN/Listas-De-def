# 9: Crie uma função que conte quantas vogais existem em uma string fornecida.

# Declaração de variaveis

palavra = input("Digite uma palavra: ").lower().strip()

# Declaração da função

def vogalometro(word, contador = 0):
    for i in range(len(word)):
        if word[i] in "aeiou":
            contador += 1

    return contador

# Apresentação de resultados

print(f"{palavra} possui {vogalometro(palavra)} vogais.")