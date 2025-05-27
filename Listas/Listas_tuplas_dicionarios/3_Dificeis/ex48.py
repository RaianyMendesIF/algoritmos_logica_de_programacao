# . Dada uma lista de n´umeros, retorne uma nova lista com os elementos ao quadrado,
# mas somente os pares.
lista = [7, 22, 71, 51, 20]
nova_lista = []

for i in lista:
    if i % 2 == 0:
        i = i**2

    nova_lista.append(i)

print(nova_lista)