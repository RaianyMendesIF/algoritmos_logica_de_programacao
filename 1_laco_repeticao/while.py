# Variável de controle
i = 0

# Enquanto - Condição de parada
while i <= 10:
    print(i, end=' ')
# Atribuição da variável de controle
    i+= 1
    
# >>> 0 1 2 3 4 5 6 7 8 9 10

print('')

j = 30
while j < 50:
    if j % 2 == 0:
        print(j, end=' ')
    j += 1
    
# >>> 30 32 34 36 38 40 42 44 46 48 

resp = 's'
while resp == 's':
    print('Ainda estou repetindo')  
    while True:
        resp = input("deseja continuar: (S) - sim / (N) - não: ")
        resp = resp.upper()
        if resp == 's' or resp == 'n':
            break  # Termina um laço de repetição
        else: 
            print("Digite uma resposta válida!!")
    
print("terminei")    