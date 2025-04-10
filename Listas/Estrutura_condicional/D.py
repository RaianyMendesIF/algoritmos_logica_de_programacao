import math

raio = float(input("Digite o raio da circunferência: "))

if raio <= 0:
    print("Valor irregular!! (raio deve ser positivo diferente de zero)")
else: 
    area = math.pi * (raio**2)
    print (f"Área da circunferência: {area}")