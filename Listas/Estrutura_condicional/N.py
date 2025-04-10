print("Digite 3 valores:  ")


numero1 = (int(input ("1º: "))) 
numero2 = (int(input ("2º: "))) 
numero3 = (int(input ("3º: "))) 

 
crescente = [numero1, numero2, numero3]  

crescente.sort()
for num in crescente:
    print(num, end=', ') 

