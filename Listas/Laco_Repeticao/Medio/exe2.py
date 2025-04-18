numero = int(input("Digite o número para verificar sé é um número perfeito:\n "))

divisores = []

for i in range(1,numero):
    if numero % i == 0:
        divisores.append(i)

soma_divisores = sum(divisores)

if soma_divisores == numero:
    
    print(f"Número perfeito")
    
else:
    print(f"Não número perfeito")
