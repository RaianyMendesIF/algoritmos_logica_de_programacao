# Implemente a ordena¸c˜ao manual de uma lista usando o algoritmo Bubble Sort.

lista = [4, 3, 2, 1]
tam = len(lista)

for i in range(tam):
    for j in range(tam - i - 1):
        if lista[j] > lista[j + 1]:    
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
    