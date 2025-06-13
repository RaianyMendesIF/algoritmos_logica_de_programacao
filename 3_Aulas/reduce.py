'''
map , filter e reduce

A função reduce() aplica uma função cumulativa aos itens de um iterável, da esquerda para a direita, reduzindo-o a um único valor.
Ela precisa ser importada do módulo functools.

Sintaxe:
from functools import reduce
reduce(funcao, iteravel)

'''

'''
from functools import reduce

# Calcular o produto de todos os números
numeros = [1, 2, 3, 4]
produto = reduce(lambda x, y: x * y, numeros)
print(produto)  # 24
'''

'''
APLICA UMA FUNÇÃO DE DOIS ARGUMENTOS
CUMULATVAMENTE AOS ITENS DE ITERÁVEL

->  Reduzir o iterável a um único valor
[2, 3, 4, 5] => 3
# PEGA UMA LISTA DA ESQUERDA PARA A DIREITA E RETORNA UM VALOR

SINTAXE
from functools import reduce
reduce (fun, array, (valor inicial))

'''

from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10) ] #Compreensão de listas; anderline omite o contador, pois não vou utiliza-lo

# x = acumulador; y= valor corrente do interável
soma_total = reduce(lambda x, y: x+y, numeros)

maior = reduce(lambda x, y: x if x > y else y, numeros) # Retona x se x>y se não retorna y

print(numeros)
print(soma_total) 
print(maior) 


