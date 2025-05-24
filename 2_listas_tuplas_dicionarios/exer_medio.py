'''
Ex3 - Crie um programa para ler o nome, a matricula e as quatro notas de 5/30 alunos e armz. em um dicionario
{matricula : nome, notas: [n1, n2, n3, n4]} as notas podem ser geradas de forma aleatória com o uso compreensão de lista

a) mostrar aluno com a maior média
b) porcentagem de alunos com maior média que 8.00
c) porcentagem de alunos reprovados, considerando média < 4 p/ reprovar
'''
from random import randint


# def generate_username():
#     characters = string.ascii_letters + string.digits + '._-'
#     username = ''.join(random.choice(characters) for _ in range(random.randint(5, 32)))
#     return username

lista_nomes = [
    "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Giovana", "Henrique", "Isabela", "João",
    "Karen", "Leonardo", "Marina", "Nicolas", "Olívia", "Paulo", "Quésia", "Rafael", "Sabrina", "Thiago",
    "Ursula", "Vinícius", "Wesley", "Xênia", "Yasmin", "Zeca", "Amanda", "Breno", "Camila", "Diego",
    "Elaine", "Fábio", "Gustavo", "Helena", "Ícaro", "Jéssica", "Kaio", "Lívia", "Murilo", "Natália",
    "Otávio", "Priscila", "Renato", "Samara", "Tales", "Valéria", "William", "Yuri", "Zuleica", "Cristina"
]


alunos = {}
maior_media = [0, '', 0]
media_maior = 0
reprovados = 0

for i in range(50):
    # print("Aluno", i+1)
    matricula = randint(1000, 9999)
    nome = lista_nomes[i]
    notas = [randint(1, 10) for x in range(4)]
    media = sum(notas) / len(notas)
    notas.append(media)
    alunos[matricula] = {nome: notas}

# Verificar se é maior média que está sendo atribuida
    if maior_media[2] < media:
        maior_media = [matricula, nome, media]

# Verificar se a média é maior que 8.00 ou menor que 4.0
    if media >= 8.00:
        media_maior +=1
    elif media < 4.00:
        reprovados += 1

 
print(alunos)

# Cáluculos em porcentagem
porc_media_maior = (len(alunos)/100) * (media_maior)

porc_reprovados = (len(alunos)/100) * (reprovados)



print("_____ LISTA DE ALUNOS _____ ")

for i in alunos.items():
    dic = i[1]
    print(f"""
_________________________
MATRÍCULA: {i[0]} """, end='')
    
    for j in dic.keys():
        print(f"""
NOME: {j} """, end='')
        
        for k in dic.values():
            print(f"""
NOTAS: {k} """, end='')






print(f"""
      
_____ ANÁLISE DE RESULTADOS  _____

Aluno destaque
    {maior_media[1]}
    Média: {maior_media[2]}

Alunos aprovados com média maior ou igual a 8.0
    {porc_media_maior} %       
      
Alunos reprovados com média menor que 4.0
    {porc_reprovados} %

""")