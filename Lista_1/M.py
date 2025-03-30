print("Digite 5 números:  ")
numeros = []

numeros.append(int(input ("1º: "))) 
numeros.append(int(input ("2º: "))) 
numeros.append(int(input ("3º: "))) 
numeros.append(int(input ("4º: "))) 
numeros.append(int(input ("5º: "))) 


impares = [numero for numero in numeros if numero % 2 != 0]

soma = 0

for numero in impares:
    soma += numero

media = soma / len(impares)

print(f"Média dos nº ímpares: {media}")