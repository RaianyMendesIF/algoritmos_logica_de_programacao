numero = int(input("Digite um número: "))

for i in range(1,numero+1):

    for k in range(4,i,-1):
        print(' ', end='')

    for j in range(1,i+1):
        print(j, end='')
    
    for l in range(i-1,0,-1):
        print(l, end='')

    print('')