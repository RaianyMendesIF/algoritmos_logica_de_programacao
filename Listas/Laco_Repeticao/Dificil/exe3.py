n = int(input("Digite um número inteiro positivo: "))
primos = []
primo = True
gemeos = ""

for i in range(3, n + 1):
    primo = True
    for j in range(2,i):

        if i % j == 0:
            primo = False
                
    if primo == True:
        primos.append(i)


for i in range(len(primos)-1):
    j = i + 1
    if primos[j] == (primos[i] + 2):
            gemeos += f"({primos[i]}, {primos[j]}), "

print(gemeos)
