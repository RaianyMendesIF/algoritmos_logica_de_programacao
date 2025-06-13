alunos = []

def cadastrar_aluno(nome, matricula, notas):
    aluno = {'nome': nome, 'matricula': matricula, 'notas': notas}
    print(aluno)
    alunos.append(aluno)
    
def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for i, aluno in enumerate(alunos):
            print(f"{i + 1}. Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Notas: {', '.join(map(str, aluno['notas']))}")
def consultar_aluno(matricula):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None



