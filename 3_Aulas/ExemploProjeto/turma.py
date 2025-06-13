turmas = []

def cadastrar_turma(nova_turma):
    turma = {
        'nome': nova_turma['nome'],
        'codigo': nova_turma['codigo'],
        'professor': nova_turma['professor'],
        'alunos': nova_turma['alunos']
    }
    turmas.append(turma)

def listar_turmas():
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
    else:
        print("Lista de Turmas:")
        for i, turma in enumerate(turmas):
            print(f"{i + 1}. Nome: {turma['nome']}, Código: {turma['codigo']}, Professor: {turma['professor']}, Alunos: {', '.join(turma['alunos'])}")

def consultar_turma(codigo):
    for turma in turmas:
        if turma['codigo'] == codigo:
            return turma
    return None

def remover_turma(codigo):
    global turmas
    turmas = [turma for turma in turmas if turma['codigo'] != codigo]
    print(f"Turma com código {codigo} removida com sucesso.")
