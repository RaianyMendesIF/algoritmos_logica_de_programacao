# Crie uma fun¸c˜ao que retorne o segundo maior n´umero de uma lista.]

numeros = [1, 5, 6, 5, 8, 18, 4, 1, 5, 44, 6, 44, 22,]
lista = numeros.copy()
maior = max(lista)
qnt = lista.count(maior)

for i in range(qnt):
    lista.remove(maior)

maior = max(lista)

print("O segundo maior valor é ", maior)