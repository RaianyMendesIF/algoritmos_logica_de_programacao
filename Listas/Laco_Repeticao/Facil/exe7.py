numero = int(input("Digite o número para verificar seus divisores: "))
qnt_divisores = 0
divisores = []
for i in range(1,numero+1):
    if numero % i == 0:
        qnt_divisores += 1
        divisores.append(i)
print(f"O número {numero} há {qnt_divisores} divisores")
print(divisores)