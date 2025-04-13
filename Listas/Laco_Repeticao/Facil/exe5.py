numero = int(input("Digite o número limite: "))
soma = 0
for i in range(1,numero+1,2):
    soma += i
    print(i)
print(f"Soma dos ímpares: {soma}")
