'''
filtra os elementos de um iterável com base em uma função que retorna True ou False.

Sintaxe:
filter(funcao, iteravel)
'''

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4, 6]