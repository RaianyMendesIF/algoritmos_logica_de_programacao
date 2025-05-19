#  Crie uma lista com 5 n´ umeros e calcule a m´edia usando la¸co for.

numeros = [1, 5, 7, 65, 98]

media = 0
for num in numeros:
     media += num
media = media / len(numeros)

print(media)