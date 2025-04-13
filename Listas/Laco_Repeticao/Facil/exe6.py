numero = int(input("Digite o número para calcular seu fatorial: "))
fatorial = 1
for i in range(1,numero+1):
    fatorial = fatorial * i
print(fatorial)
