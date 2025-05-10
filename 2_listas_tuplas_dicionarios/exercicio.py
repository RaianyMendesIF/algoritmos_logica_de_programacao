import random

"""
Pensando em listas de 50 alunos, onde serão lidas (random) 4 notas (0 - 100) mostre:
    a % de alunos aprovados
    a % de alunos reprovados
    
    imprima os 5 primeiros alunos com média mais alta
    imprime os 5 piores alunos
    imprima a nota mais alta, a posição qual aluno pertence 
    
"""   
alunos = []
notas = []

for i in range(5):
    for j in range(4):
        nota = random.randint(0,100)
        notas.append(nota)
    alunos[{i}].append({"notas": notas})

print(alunos)