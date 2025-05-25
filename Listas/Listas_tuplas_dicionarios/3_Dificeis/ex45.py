# Fa¸ca uma fun¸c˜ao que receba uma lista de listas e retorne uma lista ”achatada”(flatten).
from itertools import chain

lista_aninhada = [[1, 2], [3, 4], [5, 6]]

# lista_achatada= [item for sublista in lista_aninhada for item in sublista]

lista_achatada = list(chain.from_iterable(lista_aninhada))

print(lista_achatada)