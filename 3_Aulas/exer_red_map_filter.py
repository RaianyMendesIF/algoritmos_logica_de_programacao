from functools import reduce
from random import randint

numeros = [randint(1,10) for _ in range(10)]
print(numeros)

# EXERCÍCIO 1
# calcular a média dos quadrados dos números pares de uma lista

''' 
pares = list(filter(lambda x: x % 2 == 0, numeros))
quadrado = list(map(lambda x: x ** 2, pares))
media = reduce(lambda x, y: x+y, quadrado) / len(quadrado)
'''

media_final = reduce(lambda x, y: x+y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))
print(media_final)


# EXERCÍCIO 2
# Encontrat o maior número ímpar após elevar ao cubo

maior = max(filter(lambda x: x % 2 != 0, map(lambda x: x ** 3, numeros)))
print('Maior:', maior)


# EXERCÍCIO 3
# Somar o quadrado dos números que são múltiplos de 3
soma = reduce(lambda x, y: x+y, map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numeros)))
print('Soma:',soma)


# EXERCÍCIO 4
# Calcular o produto dos números pares após multiplicar por 2
produto = reduce(lambda x, y: x*y, map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numeros)))
print('Produto:', produto)


# EXERCÍCIO 5
# Encontrat  a média dos números que são maiores que 5 após elevar ao quadrado
media_2 = reduce(lambda x, y: x+y, map(lambda x: x ** 2, filter(lambda x: x > 5, numeros))) / len(list(filter(lambda x: x > 5, numeros)))
print('Media > 5:', media_2)


# EXERCÍCIO 6
# Calcular a soma dos cubos dos números que são menores que a média da lista 
soma_media = reduce(lambda x,y: x+y,map(lambda x: x ** 3, filter(lambda x: x <(reduce(lambda x,y: x+y, numeros) / len((numeros))), numeros)))
print('Soma da média:', soma_media)  