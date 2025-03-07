# 4: Crie uma função que calcule o fatorial de um número.

# Declaração da função

def numFatorial (num, fatorial = 1):
    for i in range(num):
        fatorial *= (i+1)

    return fatorial


# Apresentação de resultados

print(numFatorial(5))