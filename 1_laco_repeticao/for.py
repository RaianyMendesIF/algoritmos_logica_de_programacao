'''
for i in range(1):
    
    n1 = float(input("Digite a nota n1: "))
    n2 = float(input("Digite a nota n2: "))
    n3 = float(input("Digite a nota n3: "))
    n4 = float(input("Digite a nota n4: "))
    
    media = (n1 + n2 + n3 + n4) / 4
    
    print("Prox. aluno --> ")
    
    
for i in range(5, 0, -1):
    print(i) # >> 5, 4, 3, 2, 1 
    
    
# 1- Ler dois números onde o primeiro vai ser o início e o segundo o fim. Validar os números de entrada


numero_1 = int(input("Digite o início do laço: "))
numero_2 = int(input("Digite o fim do laço: "))

if numero_1> numero_2:
    aux = numero_2
    numero_2 = numero_1
    numero_1 = aux

for i in range(numero_1, (numero_2 + 1)):
    print(i)
        
'''

"""
for i in range(1,6):
    texto = ""
    for j in range(i):
        texto += "*"
    print(texto)
       

*   
**  
***
****
*****
"""
'''    
for i in range(5,0, -1):
    texto = ""
    for j in range(i):
        texto += f"{i}"
    print(texto)
    

55555
4444
333
22
1  
'''
'''
for i in range(1,6):
 
    for j in range(1,i):
        print(j, end='')
    print('')



# ler um mês e um ano qualquer, exibir o calendario completo com os dias da semana 

import calendar

yy = 2019
mm = 8

print(calendar.month(yy,mm))


'''

for i in range(6,0,-1):

    esc = 6-i
    for k in range(esc):
        print(' ', end='')

    for j in range(i):
        print("*", end=" ") 
    print('')    
    
    
    
'''
* * * * * * 
 * * * * * 
  * * * *
   * * *
    * *
     *
 '''   


