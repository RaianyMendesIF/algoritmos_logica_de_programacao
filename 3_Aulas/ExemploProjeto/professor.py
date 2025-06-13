professores = []

def cadastrar_professor(nome, matricula, disciplina):
    professor = {'nome': nome, 'matricula': matricula, 'disciplina': disciplina}
    professores.append(professor)
    
def listar_professores():
    
    
    if len(professores) == 0:
        print("Nenhum professor cadastrado.")
    else:
        print("Lista de Professores:")
        for i, professor in enumerate(professores):
            print(f"{i + 1}. Nome: {professor['nome']}, Matrícula: {professor['matricula']}, Disciplina: {professor['disciplina']}")
            
def consultar_professor(matricula):
    for professor in professores:
        if professor['matricula'] == matricula:
            return professor
    return None
def remover_professor(matricula):
    global professores
    professores = [professor for professor in professores if professor['matricula'] != matricula]
    print(f"Professor com matrícula {matricula} removido com sucesso.")


