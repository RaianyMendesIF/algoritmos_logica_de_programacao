from util import clear
from aluno import cadastrar_aluno, listar_alunos
from professor import cadastrar_professor, listar_professores
from turma import cadastrar_turma, listar_turmas


def Menu():
    print('++++++++++++ Menu ++++++++++++')
    print("1 - Cadastrar")
    print("2 - Matricular") 
    print("3 - Consultar")
    print("4 - Relatório")
    print("0 - Sair")
    op = opcao(4)

    if op == 1:
        Cadastrar()
    elif op == 2:
        Matricular()
    elif op == 3:
        Consultar()
    elif op == 4:
        Relatorio()
    elif op == 0:
        exit()

def opcao(limite):
    while True:
        try:
            op = int(input("Digite a opção desejada: "))
            if 0 <= op <= limite:
                return op
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def Cadastrar():
    print('++++++++++++ Menu Cadastro ++++++++++++')
    print("1 - Aluno")
    print("2 - Professor") 
    print("3 - Turma")
    print("0 - Voltar")
    op = opcao(3)

    if op == 1:
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        notas = input("Digite as notas do aluno separadas por vírgula: ").split(",")
        notas = [float(n.strip()) for n in notas if n.strip()]
        cadastrar_aluno(nome, matricula, notas)
        print(f"Aluno {nome} cadastrado com sucesso!")
    elif op == 2:
        nome = input("Digite o nome do professor: ")
        matricula = input("Digite a matrícula do professor: ")
        disciplina = input("Digite a disciplina: ")
        cadastrar_professor(nome, matricula, disciplina)
        print(f"Professor {nome} cadastrado com sucesso!")
    elif op == 3:
        nome = input("Digite o nome da turma: ")
        codigo = input("Digite o código da turma: ")
        professor = input("Digite o nome do professor: ")
        turma = {'nome': nome, 'codigo': codigo, 'professor': professor, 'alunos': []}
        cadastrar_turma(turma)
        print(f"Turma {nome} cadastrada com sucesso!")

def Consultar():
    print('++++++++++++ Menu Consultar ++++++++++++')
    print("1 - Aluno")
    print("2 - Professor") 
    print("3 - Turma")
    print("0 - Voltar")
    op = opcao(3)

    if op == 1:
        listar_alunos()
    elif op == 2:
        listar_professores()
    elif op == 3:
        listar_turmas()

def Matricular():
    print('++++++++++++ Menu Matrícula ++++++++++++')
    print("1 - Matricular aluno em turma")
    print("0 - Voltar")
    op = opcao(1)

    if op == 1:
        from aluno import consultar_aluno
        from turma import consultar_turma
        matricula = input("Digite a matrícula do aluno: ")
        aluno = consultar_aluno(matricula)
        if aluno is None:
            print("Aluno não encontrado.")
            return
        codigo = input("Digite o código da turma: ")
        turma = consultar_turma(codigo)
        if turma is None:
            print("Turma não encontrada.")
            return
        turma['alunos'].append(aluno['nome'])
        print(f"Aluno {aluno['nome']} matriculado na turma {turma['nome']}.")

def Relatorio():
    print('++++++++++++ Relatório de Turmas ++++++++++++')
    listar_turmas()
