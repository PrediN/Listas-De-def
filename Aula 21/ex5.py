# 5: Crie uma função chamada tabuada que recebe um número e imprime sua tabuada do 1 ao 10.

# Declaração da função

def tabuada (num):
    for i in range(10):
        print(f"{i+1}x{num} = {(i+1)*num}")
    print()
# Declaração de variaveis

numero = int(input("Digite um número: "))

# Apresentação de resultados

tabuada(numero)