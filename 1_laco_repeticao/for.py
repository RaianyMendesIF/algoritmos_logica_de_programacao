# 09/04/2025
# Leia 4 notas de X alunos e mostre a média de cada um

for i in range(1):
    
    n1 = float(input("Digite a nota n1: "))
    n2 = float(input("Digite a nota n2: "))
    n3 = float(input("Digite a nota n3: "))
    n4 = float(input("Digite a nota n4: "))
    
    media = (n1 + n2 + n3 + n4) / 4
    print(f"Média: {media}")
    print("Prox. aluno --> ")

#------------------------------------------------------------------------------------------------------------#   

# Mostrando os números do 5 ao 1 
for i in range(5, 0, -1):
    print(i) # >> 5, 4, 3, 2, 1 
    
#------------------------------------------------------------------------------------------------------------#  
    
# 1- Ler dois números onde o primeiro vai ser o início e o segundo o fim. Validar os números de entrada
numero_1 = int(input("Digite o início do laço: "))
numero_2 = int(input("Digite o fim do laço: "))

if numero_1 > numero_2:

    aux = numero_2
    numero_2 = numero_1
    numero_1 = aux

for i in range(numero_1, (numero_2 + 1)):
    print(i)
       
#------------------------------------------------------------------------------------------------------------#  

for i in range(1,6):
    texto = ""
    for j in range(i):
        texto += "*"
    print(texto)       

# *   
# **  
# ***
# ****
# ***** 

#------------------------------------------------------------------------------------------------------------#  
    
for i in range(5,0, -1):
    texto = ""
    for j in range(i):
        texto += f"{i}"
    print(texto)
    

# 55555
# 4444
# 333
# 22
# 1  

#------------------------------------------------------------------------------------------------------------#  

for i in range(7):
 
    for j in range(1,i):
        print(j, end='')
    print('')

# 1
# 12
# 123
# 1234
# 12345

#------------------------------------------------------------------------------------------------------------#  

# ler um mês e um ano qualquer, exibir o calendario completo com os dias da semana 
import calendar
yy = 2019
mm = 8
print(calendar.month(yy,mm))

#      August 2019
#  Mo Tu We Th Fr Sa Su
#            1  2  3  4
#   5  6  7  8  9 10 11
#  12 13 14 15 16 17 18
#  19 20 21 22 23 24 25
#  26 27 28 29 30 31

#------------------------------------------------------------------------------------------------------------#  

for i in range(6,0,-1):

    esc = 6-i
    for k in range(esc):
        print(' ', end='')

    for j in range(i):
        print("*", end=" ") 
    print('')    
    
      

#  * * * * * * 
#   * * * * * 
#    * * * *
#     * * *
#      * *
#       *
 

for i in range(1,4):
    # ----- Parte 1- Vazio --------   
    vazio = 3-i
    for j in range(vazio):
        print(' ',end="")
    # ----- Parte 1 - Preenchida --------   
    for k in range(i):
        print("*", end=" ")
    # ----- Parte 2 --------       
    for l in range(0,i-1):
            print("*", end=" ")
    print()

#   *
#  ***
# *****
