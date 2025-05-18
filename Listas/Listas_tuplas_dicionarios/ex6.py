# Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o maior e o menor n´umero.

numeros = []

for i in range(1,6):
    numero= int(input(f"Numero {i}: "))
    numeros.append(numero)
    
maximo = max(numeros)
minimo = min(numeros)


print(f"Número máximo : {maximo} ")
print(f"Número mínimo : {minimo} ")