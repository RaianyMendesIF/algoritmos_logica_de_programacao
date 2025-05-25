# Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.

import random

numeros = [random.randint(1, 100) for _ in range(20)]
pares = []
impares = []


for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"""
LISTAS:
INICIAL: {numeros}
PARES: {pares}
ÍMPARES: {impares}
      """)