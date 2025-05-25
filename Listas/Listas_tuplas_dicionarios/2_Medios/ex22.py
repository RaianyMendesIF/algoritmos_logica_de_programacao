# Crie uma fun¸c˜ao que recebe uma lista e retorna uma nova lista com apenas os elementos ´unicos.

def filtrar_repetidos(lista):
    filtro = set(lista)
    nova_lista = list(filtro)

    return nova_lista

lista = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6]
print(lista) # >>> [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6]
lista = filtrar_repetidos(lista)
print(lista) # >>> [1, 2, 3, 4, 5, 6]