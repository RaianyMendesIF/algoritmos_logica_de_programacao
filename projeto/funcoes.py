from functools import reduce
from utilidades import validar_opcao, lista_vazia, clear, continuar, sair
from collections import Counter #  contar a frequência de elementos em uma sequência
from evento import eventos
from usuario import usuarios

from reportlab.pdfgen import canvas  # pip install reportlab
from reportlab.lib.pagesizes import A4 # A4 = (210*mm,297*mm)

temas = [
    'Desenvolvimento Web',
    'Inteligência Artificial', 
    'Segurança',  
    'Banco de Dados', 
    'Desenvolvimento Mobile', 
    'Redes de Computadores',  
    'Linguagens de Programação',
    'Análise de Dados', 
    'Ética e Privacidade',]
tipos_evento = [
    'Workshop',
    'Maratona de Programação', 
    'Palestra', 
    'Minicurso',]

def titulo(texto):
    print(f"------------------------- {texto} -------------------------")

def gerar_id_evento():
    tam = len(eventos)
    if tam == 0:
        return tam + 1
    else:
        ultimo_id = reduce(lambda x, y: x if x > y else y, eventos.keys())
        return ultimo_id + 1
    
def gerar_id_usuario():
    tam = len(usuarios)
    if tam == 0:
        return tam + 1000
    else:
        ultimo_id = reduce(lambda x, y: x if x > y else y, usuarios.keys())
        return ultimo_id + 1

# EVENTOS

#TIPO DE EVENTO
def mostrar_tipos_evento():
    print("TIPO DE EVENTO ")
    for i,tipo in enumerate(tipos_evento):
        print(f'{i+1} - {tipo}')
    print("")

def mostrar_temas():
    print("TEMA")
    for i,tema in enumerate(temas):
        print(f'{i+1} - {tema}')
    print("0 - Adicionar tema")

# TEMAS
def selecionar_tema():
    mostrar_temas()
    op = validar_opcao(len(temas))

    if op == 0:
        clear()
        novo_tema = input("NOVO TEMA: ")
        op = adicionar_tema(novo_tema)

    return temas[op-1]

def adicionar_tema(novo_tema):
    temas.append(novo_tema)
    return len(temas)

#EVENTOS
def cadastrar_evento():
    titulo("CADASTRO DE EVENTO")
    cod = gerar_id_evento()
    
    #TIPO EVENTO
    mostrar_tipos_evento()
    op = validar_opcao(4, 1)
    tipo = tipos_evento[op-1]
    

    nome = input("NOME: ")
    palestrante = input("PALESTRANTE: ")
    max_parti = input("TOTAL PARTICIPANTES: ")
    data = input("DATA(xx/xx/xxxx): ")
    horario = input("HORÁRIO: ")
    duracao = input("DURAÇÃO: ")
    local = input("LOCAL: ")
    

    # TEMA EVENTO
    mostrar_temas()
    op = validar_opcao(len(temas))
    if op == 0:
      novo_tema = input("NOVO TEMA:")
      op = adicionar_tema(novo_tema) 
    tema = temas[op-1]

    try:
        eventos[cod] = { 'tipo' : tipo, 'nome' : nome, 'max_participantes': max_parti, 'data' : data,'hora' : horario,'duracao' : duracao,
                        'local' : local, 'tema' : tema, 'palestrante' : palestrante, 'qnt_participantes' : 0, 'participantes' : []}
        clear()
        
        print(f'EVENTO {nome} CADASTRADO COM SUCESSO! \nCÓDIGO DO EVENTO: {cod}')
    except:
        print(f'$@ NÃO FOI POSSÍVEL CADASTRAR O EVENTO {nome}! @$')
    continuar()

def verificar_evento(cod):
    if cod in eventos:
        return eventos[cod]

def listar_participantes_evento():
    titulo("PARTICIPANTES POR EVENTO") 
    cod = int(input("CÓDIGO EVENTO: "))
    if verificar_evento(cod):
        print("EVENTO: ", eventos[cod]['nome'])
        listar_participantes(cod)
    else: 
        print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()
    
def listar_participantes(cod):
    participantes = eventos[cod]['participantes']
    print(f"      ID              NOME                      EMAIL               ")
    for i,user in enumerate(participantes):
       print(f" {i} - {user}  |  {usuarios[user]['nome']}   |   {usuarios[user]['email']}")

def exibir_evento(k):
    print(f'''
 COD: {k}   |   {eventos[k]['tipo']} : {eventos[k]['nome']} 
 TEMA: {eventos[k]['tema']}   |   PARTICIPANTES: {eventos[k]['qnt_participantes']}/{eventos[k]['max_participantes']} 
 DATA: {eventos[k]['data']}   |   HORÁRIO: {eventos[k]['hora']}   |   LOCAL: {eventos[k]['local']}   |   DURAÇÃO: {eventos[k]['duracao']}''')

def listar_eventos():
    titulo("LISTAR EVENTOS")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA LISTAR!")   
    else:
        for key in eventos:
            exibir_evento(key)
        continuar()

def editar_evento():
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA EDITAR!")
    else:
        titulo("EDITAR EVENTO")
        cod = int(input("CÓD. EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod) 
            continuar()
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
                    mostrar_tipos_evento()
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
                    mostrar_temas()
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
        else:
             print("EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE!")
    continuar()

def buscar_evento():
    while True:
        titulo("BUSCAR EVENTO")
        if lista_vazia(eventos):
            print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")
            continuar()   
            return    
        else:
            cod = int(input("CÓDIGO EVENTO: "))
            if verificar_evento(cod):
                exibir_evento(cod)
                if sair("BUSCAR EVENTO") == True:
                    return
                else:
                    clear()
            else: 
                print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
                if sair("BUSCAR EVENTO") == True:
                    return
                else: 
                    clear( )
    continuar()

def remover_evento():
    global eventos
    titulo("REMOVER EVENTO")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA REMOVER!")       
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            clear()
            exibir_evento(cod)
            op = input("CONFIRMAR EXCLUSÃO(S/N): ")
            if confirmar_exclusao(op):
                try: # remover a mat das listas do curso
                    parti = eventos[cod]['participantes']
                    for mat in parti:
                        usuarios[mat]['eventos'].remove(cod)
                except:
                    print("$# NÃO FOI POSSÍVEL REMOVER O EVENTO! $#")
                    continuar()  
                try:     
                    del eventos[cod]
                    print(f" EVENTO REMOVIDO COM SUCESSO! ")
                    continuar()
                    return
                except:
                    print("$#ERRO AO REMOVER O PARTICIPANTE! $#")    
            else:
                print(f"OPERAÇÃO DE EXCLUSÃO CANCELADA! ")
                continuar()       
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()
    
    
#Verificar se um participantes está mat. no evento
def consultar_participante(cod, matricula): 
    if matricula in eventos[cod]['participantes']:
        return True
  
def temas_frequentes():
    cont = Counter() # Contador vazio (como um dicionário)
    for cod in eventos:
            tema = eventos[cod]['tema']
            cont[tema] += 1 #Incrementa 1 na contagem do tema apartir do seu id
    frequentes = cont.most_common(10) # 10 temas que mais aparecem

    titulo("TEMAS FREQUENTES")
    for tema, qnt in frequentes:
        print(f"{tema} - {qnt} eventos")
    continuar()

def participantes_mais_ativos():
    contador = Counter()  
    for cod in eventos:
        for matricula in eventos[cod]['participantes']:
            contador[matricula] += 1
    mais_ativos = contador.most_common(50)
    

    titulo("PARTICIPANTES MAIS ATIVOS")
    for matricula, qtd in mais_ativos:
        print(f"{usuarios[matricula]['nome']} - {qtd} eventos")
    
    continuar()
  

# USUÁRIOS
def listar_cursos_matriculado(mat):
    evento = usuarios[mat]['eventos']
    if lista_vazia(evento):
        print("NÃO HÁ CURSOS MATRICULADOS!")
    else:
        for even in evento:
            print(f" {even}  -  {eventos[even]['nome']}")

def criar_lista_temas(tematica):
    tema = []
    for cod in tematica:
        if cod > 0 and cod < len(temas):
            tema.append(temas[cod-1])
        if cod == 0:
            adicionar_tema()
    return tema

def cadastrar_usuario():
    titulo("CADASTRO DE USUÁRIO")
    matricula = gerar_id_usuario()
    nome = input("NOME COMPLETO: ")
    email = input("E-MAIL: ")

    tematicas = []
    op = 'S'
    while op.upper() == 'S':
        tema = selecionar_tema()
        if tema.index(tema):
            print("CURSO JÁ ADICIONADO!")
        else:
            tematicas.append(tema)
            [print(i, end='; ') for i in tematicas]
        op = input("\nDESEJA ADICIONAR MAIS TEMAS?:(S/N)")
    clear()
    usuarios[matricula] = {'nome' : nome, 'email' : email, 'temas' : tematicas, 'eventos' : []}
    print(f'USUÁRIO {nome} CADASTRADO COM SUCESSO!')
    continuar()


def verificar_usuario(mat):
    if mat in usuarios:
        return True

def exibir_usuario(mat):
    print(f'''
 MATRÍCULA: {mat}   |   NOME: {usuarios[mat]['nome']}          
 E-MAIL: {usuarios[mat]['email']} 
 PREFERÊNCIA TEMÁTICA: {", ".join(usuarios[mat]['temas'])}

 CURSOS MATRICULADOS:''')
    listar_cursos_matriculado(mat)
    print('\n+----------------------------------------------------------------------------------------------------+')

def listar_usuarios():
    titulo("LISTAR USUÁRIOS")
    if lista_vazia(usuarios):
        print("NÃO HÁ PARTICIPANTES CADASTRADOS PARA LISTAR!")   
    else:
        for mat in usuarios:
            exibir_usuario(mat)
    continuar()
             
def editar_usuario():
    titulo("EDITAR USUÁRIO")
    if lista_vazia(usuarios):
        print("NÃO HÁ USUÁRIOS CADASTRADOS PARA EDITAR!")
        continuar()
    else:
        titulo("EDITAR USUÁRIO")
        mat = int(input("MATRÍCULA USUÁRIO: "))
        if verificar_usuario(mat):
            exibir_usuario(mat)
            continuar()
            while True:    
                print(f'''
+----------------------------+
|           EDITAR           |
+----------------------------+
| 1 - NOME                   |
| 2 - EMAIL                  |
| 3 - PREFERÊNCIA TEMÁTICA   |   
| 0 - SAIR                   |
+----------------------------+   ''')

                op = validar_opcao(3)
                clear()
                if op == 1:
                    print("_____ EDITAR NOME _____")
                    nome = input("NOVO NOME: ")
                    clear()
                    try:
                        usuarios[mat]['nome'] = nome 
                        print(f"NOME ALTERADO PARA {nome} COM SUCESSO!")
                    except:
                        print("$@ NÃO FOI POSSÍVEL ALTERAR O NOME DO PARTICIPANTE! @$")
                    continuar()

                if op == 2:
                    print("_____ EDITAR E-MAIL _____")
                    email = input("NOVO E-MAIL: ")
                    clear()
                    try:
                        eventos[mat]['email'] = email 
                        print(f"EMAIL ALTERADO PARA {email} COM SUCESSO!")
                    except:
                        print("$@ NÃO FOI POSSÍVEL ALTERAR O EMAIL DO PARTICIPANTE! @$")
                    continuar()

                if op == 3:
                    print("_____ EDITAR PREFERÊNCIA TEMÁTICA _____")
                    mostrar_temas()
                    tematica = input("CÓD. PREFERÊNCIAS TEMÁTICA (cód. separados por vírgula ex: 1,5,...): ")
                    tematica =[int(tema.strip()) for tema in tematica.split(",")]
                    temas = criar_lista_temas(tematica)
                    clear()

                    try:
                        eventos[mat]['temas'] = temas 
                        print(f"PREFERÊNCIA TEMÁTICA ALTERADO PARA {[print(", ".join(temas))]} COM SUCESSO!")
                    except:
                        print("$@ NÃO FOI POSSÍVEL ALTERAR A PREFERÊNCIA TEMÁTICA DO PARTICIPANTE! @$")
                    continuar()

                if op == 0:
                    return

        else:
                print("USUÁRIO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE!")
        continuar()

def buscar_usuario():
    titulo("BUSCAR USUÁRIO")
    if lista_vazia(usuarios):
             print("NÃO HÁ USUÁRIOS CADASTRADOS PARA BUSCAR!")
    else:
        matricula = int(input("MATRÍCULA USUÁRIO: "))
        if matricula in usuarios:
            exibir_usuario(matricula)
        else:
            print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! #$")
    continuar()

def retornar_nome_usuario(matricula):
    return usuarios[matricula]['nome']

def remover_usuario():
    global usuarios
    titulo("REMOVER PARTICIPANTE")
    if lista_vazia(usuarios):
        print("NÃO HÁ USUÁRIOS CADASTRADOS PARA REMOVER!")       
    else:
        mat = int(input("MATRÍCULA PARTICIPANTE: "))
        if verificar_usuario(mat):
            clear()
            exibir_usuario(mat)
            op = input("CONFIRMAR EXCLUSÃO(S/N): ")
            if confirmar_exclusao(op):
                try: # remover a mat das listas do curso
                    cursos = usuarios[mat]['eventos']
                    for cod in cursos:
                        eventos[cod]['participantes'].remove(mat)
                except:
                    print("$# NÃO FOI POSSÍVEL REMOVER O PARTICIPANTE! $#")
                    continuar() 
                    return 
                try:     
                    del usuarios[mat]
                    print(f" USUÁRIO REMOVIDO COM SUCESSO! ")
                    continuar()
                    return
                except:
                    print("$#ERRO AO REMOVER O PARTICIPANTE! $#")            
            else:
                print(f"OPERAÇÃO DE EXCLUSÃO CANCELADA! ")
                return       
        else: 
            print("$# USUÁRIO NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
    continuar()


# MATRÍCULA

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

def confirmar_exclusao(op):
    if op.upper() == "S":
        return True



# EXPORTAR PDFs A4 = (210*mm,297*mm)
#Função para converter mm em pontos  
def mm2p(milimitros):
    return milimitros / 0.3527777

def exportar_lista_eventos(nome):
    try:
        doc = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        doc.drawString(mm2p(75),mm2p(y), "LISTA DE EVENTOS")
        y -= 10
 
        for key in eventos.keys():
            if y < 50:
                doc.showPage()
                y=287
            doc.drawString(mm2p(x1),mm2p(y), f"COD: {key}  |   EVENTO: {eventos[key]['tipo']} - {eventos[key]['nome']} ")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"TEMA: {eventos[key]['tema']}   |   MINISTRADOR: {eventos[key]['palestrante']}")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"DATA: {eventos[key]['data']}  |   HORA: {eventos[key]['hora']}   |   DURAÇÃO: {eventos[key]['duracao']} ")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"LOCAL: {eventos[key]['local']}   |  PARTICIPANTES: {eventos[key]['qnt_participantes']}/{eventos[key]['max_participantes']}")
            y -= 6
            doc.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        doc.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")

def exportar_lista_usuarios(nome):
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE USUÁRIOS")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), "   ID   |                 NOME                  |               E-MAIL          |         QUANTIDADES DE EVENTOS        ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for key in usuarios.keys():
            if y < 25:
                use.showPage()
                y = 287
                use.drawString(mm2p(x1), mm2p(y), "   ID   |            NOME            |            E-MAIL          |        QUANTIDADES DE EVENTOS        ")
            use.drawString(mm2p(x1), mm2p(y), f"  {key} |   {usuarios[key]['nome']}   |   {usuarios[key]['email']}  |   {len(usuarios[key]['eventos'])}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")

def exportar_participante_evento(nome,cod):
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE PARTICIPANTES POR EVENTO")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f"EVENTO: {eventos[cod]['tipo']} - {eventos[cod]['nome']}  |  COD: {cod}")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for user in eventos[cod]['participantes']:
            if y < 25:
                use.showPage()
                y = 287
                use.drawString(mm2p(x1), mm2p(y), f"EVENTO: {eventos[cod]['tipo']} - {eventos[cod]['nome']}  |  COD: {cod}")
                y -= 3
                use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            use.drawString(mm2p(x1), mm2p(y), f"  {user}      {usuarios[user]['nome']}       {usuarios[user]['email']}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")

def exportar_participante_ativo(nome):
    cont = Counter()  
    for cod in eventos:
        for matricula in eventos[cod]['participantes']:
            cont[matricula] += 1
    mais_ativos = cont.most_common(50)
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE PARTICIPANTES MAIS ATIVOS")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f" ID    |            PARTICIPANTE                |         QUANTIDADE DE EVENTOS      ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for usua, qnt in mais_ativos:
            if y < 25:
                use.showPage()
                y = 287
            use.drawString(mm2p(x1), mm2p(y), f"{usua}      {usuarios[usua]['nome']}                 {qnt}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")

def exportar_temas_frequente(nome):
    cont = Counter() 
    for cod in eventos:
            tema = eventos[cod]['tema']
            cont[tema] += 1 
    frequentes = cont.most_common(10)
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE TEMAS FREQUENTES")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f"          TEMA                |         QUANTIDADE DE EVENTOS      ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for tema, qnt in frequentes:
            if y < 20:
                use.showPage()
                y = 287
            use.drawString(mm2p(x1), mm2p(y), f"{tema}                             {qnt}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")

def verificar_usuarios():
    if len(usuarios) == 0:
        return False
    else:
        return True
    
def verificar_eventos():
    if len(eventos) == 0:
        return False
    else:
        return True