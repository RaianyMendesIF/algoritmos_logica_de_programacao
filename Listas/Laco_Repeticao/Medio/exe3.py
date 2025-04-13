num = int(input("Digite o número final(n): "))
soma = 0
expre = ""
for n in range(1,num+1):
    soma += (n / ((2*n)- 1))  

print(soma)