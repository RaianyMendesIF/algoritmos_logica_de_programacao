print("Digite 4 números:  ")
numeros = []

numeros.append(int(input ("1º: "))) 
numeros.append(int(input ("2º: "))) 
numeros.append(int(input ("3º: "))) 
numeros.append(int(input ("4º: "))) 


pares = [numero for numero in numeros if numero % 2 == 0]

resultado = 0

for numero in pares:
    resultado += numero

print(f"Soma dos pares: {resultado}")