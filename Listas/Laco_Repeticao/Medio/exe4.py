numero = int(input("Digite o número inteiro: "))

for i in range(numero+1,0,-1):
    for j in range(1,i):
        print(j, end='')
    print('')