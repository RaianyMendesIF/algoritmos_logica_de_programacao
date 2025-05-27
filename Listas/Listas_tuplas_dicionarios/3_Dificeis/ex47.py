# Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene anotas pela 
# nota em ordem decrescente
notas = []

for i in range(2):
    nome = input("NOME: ")
    nota = int(input("NOTA: "))
    notas.append((nome, nota))

tam = len(notas)

for i in range(tam):
    for j in range(tam - i - 1):
        if notas[j] < notas[j + 1]:    
            notas[j], notas[j + 1] = notas[j + 1], notas[j]

for item in notas:
    print(f"{item[0]} - {item[1]}")