# 2: Crie uma função que receba um número e retorne "Par" se o número for par ou "Ímpar" se o número for ímpar.

# Declaração de função

def parImpar (a):
    if a % 2 ==0:
        print("Par")
    else:
        print("Ímpar")

# Declaração de variavel

num = int(input("Digite um número: "))

# Apresentação de resultados

parImpar(num)