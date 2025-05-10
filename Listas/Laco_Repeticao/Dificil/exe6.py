numero = int(input("Digite um número: "))
resultado = 0

for i in range(1, numero + 1):
    if i % 2 == 0:  
        resultado -= 1 / i
    else:  
        resultado += 1 / i

print(f"Série Harmônica Alternada: {resultado}")