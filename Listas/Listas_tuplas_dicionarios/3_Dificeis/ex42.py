#  Dada uma lista de inteiros, crie uma fun¸ c˜ao que identifique os n´ umeros que aparecem mais de uma vez e 
# quantas vezes cada um aparece.
import random

# lista = [random.randint(1, 100) for _ in range(10)]
# print(lista)

lista = [76, 42, 41, 75, 65, 75, 65, 6, 75, 12]
 
def idenficar_itens(lista):
    identificados = []
    for i in lista:

        qnt = lista.count(i)
        ident = identificados.count(i)

        if (qnt > 1) and (ident == 0):
            identificados.append(i)
            print(f"O item {i} aparece {qnt} vezes.")


idenficar_itens(lista)