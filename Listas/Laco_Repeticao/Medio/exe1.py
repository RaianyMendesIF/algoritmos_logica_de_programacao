frase = input("Digite uma frase: ")
vogais = 0

for letra in frase:
    l = letra.upper()
    
    if (l == "A") or (l == "E") or (l == "I") or (l == "O") or (l == "U"):
        vogais += 1

print(f" A frase '{frase}' possui {vogais} vogais")