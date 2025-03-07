# 1. Crie uma função que recebe duas palavras e retorna True se forem anagramas uma da outra.


# Declaração da função

def anagrama(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    else:
        return sorted(palavra1) == sorted(palavra2)
    

# Declaração de variavel

palavra1 = str(input("Insira a primeira palavra: ")).lower().strip()
palavra2 = str(input("Insira a segunda palavra: ")).lower().strip()

# Apresentação de resultados

anagrama(palavra1, palavra2)