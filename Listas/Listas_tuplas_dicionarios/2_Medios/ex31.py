# Crie uma fun¸c˜ao que verifique se uma lista est´a ordenada.

lista = [1, 2, 3, 4, 5, 6, 7] 

lista_ordenada = lista.copy()
lista_ordenada.sort()

if lista == lista_ordenada:
    print(f"A lista {lista} entá ordenada!")
else:
    print(f"A lista {lista} não entá ordenada!")
