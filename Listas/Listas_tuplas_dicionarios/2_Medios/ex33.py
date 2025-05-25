# Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3.

numeros = [i for i in range(1,101)]

print("Múltiplos de 3 no intervalo de 1 - 100")
for n in numeros:
    if n % 3 == 0:
        print(n, end='; ')