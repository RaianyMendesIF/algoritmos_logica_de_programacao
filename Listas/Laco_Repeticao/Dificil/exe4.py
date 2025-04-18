
n = int(input("Digite um número inteiro positivo: "))
primos = []
primo = True
multiplos = []
resultado = n

for i in range(2, n + 1):
    primo = True
    for j in range(2,i):

        if i % j == 0:
            primo = False
                
    if primo == True:
        primos.append(i)


for i in primos:
    while resultado != 0:
        if resultado % i == 0:
            resultado = resultado / i
            multiplos.append(i)
        else:
            break
        
            
for j in multiplos: 
    print(j, end= ' * ' )
  



    