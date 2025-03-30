print("Digite 3 valores:  ")


numero1 = (int(input ("1º: "))) 
numero2 = (int(input ("2º: "))) 
numero3 = (int(input ("3º: "))) 

if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(f"Ordem crescente: {numero3}, {numero2} e {numero1}")
    elif numero3 > numero2: 
        print(f"Ordem crescente: {numero2}, {numero3} e {numero1}")


elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(f"Ordem crescente: {numero3}, {numero1} e {numero2}")
    elif numero3 > numero1: 
        print(f"Ordem crescente: {numero1}, {numero3} e {numero2}")


elif numero3 > numero1 and numero3 > numero2:
    if numero1 > numero2:
        print(f"Ordem crescente: {numero2}, {numero1} e {numero3}")
    elif numero2 > numero1: 
        print(f"Ordem crescente: {numero1}, {numero2} e {numero3}")