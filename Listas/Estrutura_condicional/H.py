medida1 =float(input("Medida 1:  "))
medida2 =float(input("Medida 2:  "))
medida3 =float(input("Medida 3:  "))

max = 0.00

for numero in (medida1, medida2, medida3):

    if max < numero:
        max = numero
        
print(f"Maior medida: {max}")
