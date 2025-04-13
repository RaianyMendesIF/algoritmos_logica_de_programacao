import string
alfabeto = list(string.ascii_uppercase)

numero = int(input("Digite um número ímper: "))


parte_1 = int(((numero - 1) / 2 ) + 1)
parte_2 = numero - parte_1

for i in range(parte_1):
    for j in range(i):
        print(alfabeto[j], end='')

    for k in range(0,i):
        print(alfabeto[k], end='')
    
    print(alfabeto[i])

for i in range(parte_2-1,-1,-1):
    for j in range(i):
        print(alfabeto[j], end='')
    print(alfabeto[i])