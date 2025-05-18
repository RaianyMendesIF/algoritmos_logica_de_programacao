# 2. Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome em uma linha

nomes = []

for i in range(1,6):
    nome = input(f"Nome {i}: ")
    nomes.append(nome)

for nome in nomes:
    print(nome)