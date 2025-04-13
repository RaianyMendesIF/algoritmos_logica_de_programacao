n = int(input("Digite um número inteiro positivo: "))
primos = []
primo = True
multiplos = []
resultado = n

for i in range(3, n + 1):
    primo = True
    for j in range(2,i):

        if i % j == 0:
            primo = False
                
    if primo == True:
        primos.append(i)


  
    while resultado != 0:
        for i in primos:  
            while n % i == 0:
                resultado = n / i
                multiplos.append(i)
                n = resultado

print(primos)
print(multiplos)

    