
def listar_eventos_matriculado(usuario, mat):
    evento = usuario[mat]['eventos']
    if lista_vazia(evento):
        print("NÃO HÁ CURSOS MATRICULADOS!")
    else:
        print(" CURSOS MATRICULADOS")
        for even in evento:
            print(f" {even}  -  {eventos[even]['nome']}")


from funcoes_tema import temas, tipos_evento, listar_tipos_evento, listar_temas, adicionar_tema
from functools import reduce
from utilidades import validar_opcao, clear, continuar, lista_vazia, titulo
from funcoes_usuario import usuarios, verificar_usuario, exibir_usuario
from dados.eventos import eventos


def gerar_id_evento():
    tam = len(eventos)
    if tam == 0:
        return tam + 1
    else:
        ultimo_id = reduce(lambda x, y: x if x > y else y, eventos.keys())
        return ultimo_id + 1

def cadastrar_evento(tipo, nome, palestrante, max_parti, data, horario, duracao, local, tema):
    cod = gerar_id_evento()
    try:
        eventos[cod] = { 'tipo' : tipo, 'nome' : nome, 'max_participantes': max_parti, 'data' : data,'hora' : horario,'duracao' : duracao,
                        'local' : local, 'tema' : tema, 'palestrante' : palestrante, 'qnt_participantes' : 0, 'participantes' : []}
        clear()
        
        print(f'EVENTO {nome} CADASTRADO COM SUCESSO! \nCÓDIGO DO EVENTO: {cod}')
    except:
        print(f'$@ NÃO FOI POSSÍVEL CADASTRAR O EVENTO {nome}! @$')
    continuar()


def exibir_evento(k, participante= False):
    print(f'''
 COD: {k}   |   {eventos[k]['tipo']} : {eventos[k]['nome']} 
 TEMA: {eventos[k]['tema']}   |   PARTICIPANTES: {eventos[k]['qnt_participantes']}/{eventos[k]['max_participantes']} 
 DATA: {eventos[k]['data']}   |   HORÁRIO: {eventos[k]['hora']}   |   LOCAL: {eventos[k]['local']}   |   DURAÇÃO: {eventos[k]['duracao']}
''')

    if participante == True:
        if lista_vazia(eventos[k]['participantes']):
            print(" NÃO HÁ PARTICIPANTES MATRICULADOS!")
        else:
            print(" PARTICIPANTES MATRICULADOS")
            listar_participantes(k)
    print('+----------------------------------------------------------------------------------------------------+')

def listar_eventos():
    titulo("LISTAR EVENTOS")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA LISTAR!")
        continuar()   
    else:
        for key in eventos:
            exibir_evento(key)
        continuar()

def editar_evento(cod):
    while True:    
        print(f'''
+----------------------------+
|           EDITAR           |
+----------------------------+
| 1 - NOME                   |
| 2 - TIPO                   |
| 3 - TEMA                   |
| 4 - TOTAL PARTICIPANTES    |
| 5 - PALESTRANTE            |
| 6 - DATA                   |
| 7 - HORA                   |    
| 8 - LOCAL                  |    
| 9 - DURAÇÃO                |    
| 0 - SAIR                   |
+----------------------------+   ''')

        op = validar_opcao(9)
        clear()

        if op == 1:
            titulo("EDITAR NOME")
            nome = input("NOVO NOME: ")
            clear()
            try:
                eventos[cod]['nome'] = nome 
                print(f"NOME DO EVENTO ALTERADO PARA {nome} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O NOME DO EVENTO! @$")
            continuar()

        if op == 2:
            titulo("EDITAR TIPO DE EVENTO")
            #TIPO EVENTO
            listar_tipos_evento()
            op = validar_opcao(4,1)
            tipo = tipos_evento[op-1]
            clear()
            try:
                eventos[cod]['tipo'] = tipo 
                print(f"TIPO DO EVENTO ALTERADO PARA {tipo} COM SUCESSO!")
            except:
                print("!@ NÃO FOI POSSÍVEL ALTERAR O TIPO DE EVENTO @!")
            continuar()
                
        if op == 3:
            titulo("EDITAR TEMA")
            # TEMA EVENTO
            listar_temas()
            op = validar_opcao(len(temas))
            clear()
            if op == 0:
                novo_tema = input("NOVO TEMA:")
                op = adicionar_tema(novo_tema) 
            tema = temas[op-1]
            try:
                eventos[cod]['tema'] = tema 
                print(f"TEMA DO EVENTO ALTERADO PARA {tema} COM SUCESSO!")
            except:
                print(f"!@ {tema} NÃO FOI POSSÍVEL ALTERAR O TEMA @!")
            continuar()

        if op == 4:
            titulo("EDITAR TOTAL DE PARTICIPANTES")
            max_participantes = int(input("NOVO TOTAL DE PARTICIPANTES: "))
            clear()
            try:
                if eventos[cod]['qnt_participantes'] > max_participantes:
                    print("#@ NÃO FOI POSSÍVEL REALIZAR A ALTERAÇÃO, POIS HÁ MAIS PARTICIPANTES MATRICULADOS DO QUE O NOVO LIMITE! @#")
                else:
                    eventos[cod]['max_participantes'] = max_participantes 
                    print(f"TOTAL DE PARTICIPANTES DO EVENTO ALTERADO PARA {max_participantes} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O TOTAL DE PARTICIPANTES DO EVENTO! @$")
            continuar()

        if op == 5:
            titulo("EDITAR PALESTRANTE")
            palestrante = input("NOVO PALESTRANTE: ")
            clear()
            try:
                eventos[cod]['palestrante'] = palestrante 
                print(f"PALESTRANTE DO EVENTO ALTERADO PARA {palestrante} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O PALESTRANTE DO EVENTO! @$")
            continuar()

        if op == 6:
            titulo("EDITAR DATA")
            data = input("NOVA DATA: ")
            clear()
            try:
                eventos[cod]['data'] = data 
                print(f"DATA DO EVENTO ALTERADO PARA {data} COM SUCESSO!")
            except:
                print("!@ NÃO FOI POSSÍVEL ALTERAR A DATA @!")
            continuar()

        if op == 7:
            titulo("EDITAR HORÁRIO")
            horario = int(input("NOVO HORÁRIO: "))
            clear()
            try:
                eventos[cod]['hora'] = horario
                print(f"HORÁRIO DO EVENTO ALTERADO PARA {max_participantes} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O HORÁRIO DO EVENTO! @$")
            continuar()
                
        if op == 8:
            titulo("EDITAR LOCAL")
            local = int(input("NOVO LOCAL: "))
            clear()
            try:
                eventos[cod]['local'] = local
                print(f"LOCAL DO EVENTO ALTERADO PARA {local} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O LOCAL DO EVENTO! @$")
            continuar()

        if op == 9:
            titulo("EDITAR DURAÇÃO")
            duracao = int(input("NOVa DURAÇÃO: "))
            clear()
            try:
                eventos[cod]['duracao'] = duracao
                print(f"DURAÇÃO DO EVENTO ALTERADO PARA {duracao} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR A DURAÇÃO DO EVENTO! @$")
                continuar()

        if op == 0:
            return 
        
def remover_evento(cod):
    del eventos[cod]
   
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
    
def verificar_evento(cod):
    if cod in eventos:
        return eventos[cod]
