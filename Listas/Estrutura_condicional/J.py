sexo = input("Sexo(F)(M): ").upper
altura = float(input("Altura: "))

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal: {peso_ideal}")
elif sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal: {peso_ideal}")
else:
    print("Valor inválido")