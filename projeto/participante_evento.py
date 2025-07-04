from utilidades import lista_vazia, continuar
from evento import eventos
from usuario import usuarios


def listar_eventos_matriculado(mat):
    evento = usuarios[mat]['eventos']
    if lista_vazia(evento):
        print("NÃO HÁ CURSOS MATRICULADOS!")
    else:
        print(" CURSOS MATRICULADOS")
        for even in evento:
            print(f" {even}  -  {eventos[even]['nome']}")

def adicionar_participante(cod, mat):
    try:
        eventos[cod]['participantes'].append(mat)
        print("PARTICIPANTE MATRICULADO COM SUCESSO!")
        continuar()
        return
    except:
        print("$# NÃO FOI POSSÍVEL MATRICULAR O PARTICIPANTE! $#")
        continuar()

def remover_usuario_cursos(cursos, mat):
    for cod in cursos:
        eventos[cod]['participantes'].remove(mat)