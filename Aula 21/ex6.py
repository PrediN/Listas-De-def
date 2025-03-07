'''
6: Crie uma função que receba uma string e retorne True se ela for
um palíndromo (uma palavra ou frase que se lê da mesma forma de trás para frente) e False caso contrário.
'''

# Declaração de função

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
# Declaração de varaveis

frase = str(input("Insira uma palavra: "))

# Apresentação de resultados

print(palindromo(frase))