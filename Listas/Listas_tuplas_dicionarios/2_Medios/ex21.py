#  Solicite ao usu´ ario 10 n´ umeros, armazene em uma lista e remova todos os n´ umeros pares usando remove
numeros = []

for i in range(1,11):
    num = int(input(f"{i} - Digite um número: "))
    numeros.append(num)

for i in reversed(numeros):
    if i % 2 == 0:
        numeros.remove(i)

print(numeros)


