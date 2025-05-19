#  Leia 5 n´ umeros do usu´ ario e verifique se cada um deles ´ e maior que 10.

numeros = []

for i in range(1,6):
    num = int(input(f"{i} - Digite um número: "))
    numeros.append(num)

for i, num in enumerate(numeros):
    if num > 10:
        print(f"{i+1} - {num} é maior que 10")
    else:
        print(f"{i+1} - {num} é menor que 10")