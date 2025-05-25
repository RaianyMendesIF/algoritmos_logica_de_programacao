# Fa¸ca um programa que leia n´umeros do usu´ario at´e digitar -1. Depois, imprima a m´edia.

numeros = []
num = 0
i = 1
while num != -1:
    num = int(input(f"Número {i}:  "))
    numeros.append(num)
    i += 1

media = sum(numeros) / len(numeros)

print(numeros)
print("Madia dos valores da lista: ", media)