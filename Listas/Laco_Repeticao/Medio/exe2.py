numero = int(input("Digite o número para verificar sé é um número perfeito:\n "))

divisores = []
soma_divisores = 0

for i in range(1,numero):
    if numero % i == 0:
        divisores.append(i)

for i in divisores:
    soma_divisores += i

if soma_divisores == numero:
    
    print(f"Número perfeito")
    
else:
    print(f"Não número perfeito")
