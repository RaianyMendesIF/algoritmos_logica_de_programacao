numero = int(input("Digite um número:"))

print(f"Número: {numero}")

if (numero >= 0) or (numero <= 20):
    print("O número está no intervalo A (0 a 20)")

elif (numero >= -5) or (numero <= -1):
    print("O número está no intervalo B (-5 a -1)")

elif (numero >= 21) or (numero <= 60):
    print("O número está no intervalo C (21 a 60)")

if (numero >= -100) or (numero <= 15):
    print("O número está no intervalo D (-100 a 15)")

