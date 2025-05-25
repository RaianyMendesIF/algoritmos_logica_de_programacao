# Implemente uma fun¸c˜ao que conte quantas vezes um valor aparece em uma lista.

def contar_itens(lista, item):
    qnt = lista.count(item)
    return f"O item {item} aparece {qnt} vezes na lista {lista}"

lista = [1, 1, 1, 2, 2, 2, 5, 5, 9 ]

print(contar_itens(lista, 5))
#>>> O item 5 aparece 2 vezes na lista [1, 1, 1, 2, 2, 2, 5, 5, 9]