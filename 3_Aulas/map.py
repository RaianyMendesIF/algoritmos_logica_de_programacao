'''

Aplica uma função a cada item de um iterável (como uma lista) e retorna um iterador com os resultados.
Sintaxe:
map(funcao, iteravel)
'''

# Dobrar os números de uma lista
numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
print(list(dobro))  # [2, 4, 6, 8, 10]