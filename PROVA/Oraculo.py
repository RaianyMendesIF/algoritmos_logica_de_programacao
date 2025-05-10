eq = 0
ins = 0

for i in range(8):
    numero = int(input("Digite o número inteiro: "))
    
    if (numero % 2 == 0 and numero % 5 == 0) or (numero % 2 != 0 and numero % 3 == 0):
        print("Numero equilibrado")
        eq += 1
    else:
        ins += 1
        
print(f"Total de num eq. = {eq}")
print(f"Total de num ins. {ins}")