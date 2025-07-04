from utilidades import lista_vazia, continuar, clear
from evento import eventos, verificar_evento, exibir_evento
from usuario import usuarios, verificar_usuario, exibir_usuario


def listar_eventos_matriculado(mat):
    evento = usuarios[mat]['eventos']
    if lista_vazia(evento):
        print("NÃO HÁ CURSOS MATRICULADOS!")
    else:
        print(" CURSOS MATRICULADOS")
        for even in evento:
            print(f" {even}  -  {eventos[even]['nome']}")

def adicionar_participante():
    print("_____ ADICIONAR PARTICIPANTE _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA ADICIONAR PARTICIPANTE!")    
        continuar()   
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod)
            continuar()
            clear()
            if lista_vazia(usuarios):
                print("NÃO HÁ USUÁRIOS CADASTRADOS PARA ADICIONAR!")    
                continuar()   
            else:
                mat = int(input("MATRÍCULA PARTICIPANTE: "))
                if verificar_usuario(mat):
                    if consultar_participante(cod, mat):
                            print("PARTICIPANTE JÁ ESTÁ MATRICULADO NESSE EVENTO!")
                    else:
                        exibir_usuario(mat)
                        continuar()
                        clear()
                        try:
                            eventos[cod]['participantes'].append(mat)
                            print("PARTICIPANTE MATRICULADO COM SUCESSO!")
                            continuar()
                            return
                        except:
                            print("$# NÃO FOI POSSÍVEL MATRICULAR O PARTICIPANTE! $#")
                            continuar()
                        return
                else:
                    print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
                continuar()
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
            continuar()


def remover_participante():
    print("_____ REMOVER PARTICIPANTE _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA REMOVER PARTICIPANTES!")    
        continuar()
        return
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod)
            continuar()
            if lista_vazia(eventos[cod]['participantes']):
                print("NÃO HÁ PARTICIPANTES CADASTRADOS PARA REMOVER!")       
            else:
                while True:
                    clear()
                    exibir_evento(cod)
                    mat = int(input("\nMATRÍCULA NOVO PARTICIPANTE: "))
                    if verificar_usuario(mat):
                        if consultar_participante(cod, mat):
                            print("PARTICIPANTE JÁ ESTÁ MATRICULADO NESSE EVENTO!")
                        else:
                            exibir_usuario(mat)
                            continuar()
                            clear()
                            try:
                                eventos[cod]['participantes'].remove(mat)
                                print(f"PARTICIPANTE REMOVIDO DO CURSO {eventos[cod]['nome']} COM SUCESSO!")
                                continuar()
                                return
                            except:
                                print("$# NÃO FOI POSSÍVEL REMOVER O PARTICIPANTE! $#")
                                continuar()

                                return
                    else:
                        print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
                    continuar()
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()


def remover_usuario_cursos(cursos, mat):
    for cod in cursos:
        eventos[cod]['participantes'].remove(mat)

#Verificar se um participantes está mat. no evento
def consultar_participante(cod, matricula): 
    if matricula in eventos[cod]['participantes']:
        return True
    
def listar_participantes(cod):
    participantes = eventos[cod]['participantes']
    print(f"      ID              NOME                      EMAIL               ")
    for i,user in enumerate(participantes):
       print(f" {i} - {user}  |  {usuarios[user]['nome']}   |   {usuarios[user]['email']}")

def remover_evento_usuarios(cod):
    try: # remover a mat das listas do curso
        parti = eventos[cod]['participantes']
        for mat in parti:
            usuarios[mat]['eventos'].remove(cod)
    except:
        print("$# NÃO FOI POSSÍVEL REMOVER O EVENTO! $#")
        continuar()  
    