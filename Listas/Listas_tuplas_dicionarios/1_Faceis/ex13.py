# Crie uma lista com os n´ umeros de 1 a 10 usando range() e imprima somente os pares
numeros = []

for i in range(1,11):
 numeros.append(i)

#Pares
for num in numeros:
    if num % 2 == 0:
       print(num, end=", ")
