from utilidades import validar_opcao, lista_vazia, clear, continuar
from collections import Counter #  contar a frequência de elementos em uma sequência
from evento import eventos, tipos_evento, temas
from usuario import usuarios

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
    print("_____ CADASTRO DE EVENTO _____")
    cod = len(eventos) + 1
    nome = input("NOME: ")

    #TIPO EVENTO
    mostrar_tipos_evento()
    op = validar_opcao(4, 1)
    tipo = tipos_evento[op-1]

    data = input("DATA(xx/xx/xxxx): ")

    # TEMA EVENTO
    mostrar_temas()
    op = validar_opcao(len(temas))
    if op == 0:
      novo_tema = input("NOVO TEMA:")
      op = adicionar_tema(novo_tema)
    tema = temas[op-1]
    try:
        eventos[cod] = {'nome' : nome, 'tipo' : tipo, 'data' : data, 'tema' : tema, 'participantes' : []}
        clear()
        print(f'EVENTO {nome} CADASTRADO COM SUCESSO!')
    except:
        print(f'$@ NÃO FOI POSSÍVEL CADASTRAR O EVENTO {nome}! @$')
    continuar()

def verificar_evento(cod):
    if cod in eventos:
        return eventos[cod]

def listar_participantes_evento():
    print("_____ PARTICIPANTES POR EVENTO _____")
    cod = int(input("CÓDIGO EVENTO: "))
    if verificar_evento(cod):
        print("EVENTO: ", eventos[cod]['nome'])
        listar_participantes(cod)
    else: 
        print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()
    
def listar_participantes(cod):
    participantes = eventos[cod]['participantes']
    for i,user in enumerate(participantes):
        print(f"{i+1} - {usuarios[user]['nome']}  /  {usuarios[user]['email']}")

def exibir_evento(k):
    print(f'''
 COD: {k} | NOME: {eventos[k]['nome']} | TIPO: {eventos[k]['tipo']}      
 DATA: {eventos[k]['data']} | TEMA: {eventos[k]['tema']}              
 PARTICIPANTES: 
 {listar_participantes(k)} 

+--------------------------------------------------------------+''')

def listar_eventos():
    print("_____ LISTAR EVENTOS _____")
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
        print("_____ EDITAR EVENTO _____")
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
| 3 - DATA                   |
| 4 - TEMA                   |    
| 0 - SAIR                   |
+----------------------------+   ''')

                op = validar_opcao(4)
                clear()

                if op == 1:
                    print("_____ EDITAR NOME _____")
                    nome = input("NOVO NOME: ")
                    clear()
                    try:
                        eventos[cod]['nome'] = nome 
                        print(f"NOME DO EVENTO ALTERADO PARA {nome} COM SUCESSO!")
                    except:
                        print("$@ NÃO FOI POSSÍVEL ALTERAR O NOME DO EVENTO! @$")
                    continuar()

                if op == 2:
                    print("_____ EDITAR TIPO DE EVENTO _____")
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
                    print("_____ EDITAR DATA _____")
                    data = input("NOVA DATA: ")
                    clear()
                    try:
                        eventos[cod]['data'] = data 
                        print(f"DATA DO EVENTO ALTERADO PARA {data} COM SUCESSO!")
                    except:
                        print("!@ NÃO FOI POSSÍVEL ALTERAR A DATA @!")
                    continuar()

                if op == 4:
                    print("_____ EDITAR TEMA _____")
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

                if op == 0:
                    return 
        else:
             print("EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE!")
    continuar()

def buscar_evento():
    print("_____ BUSCAR EVENTO _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")       
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod) 
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()

def remover_evento():
    global eventos
    print("_____ REMOVER EVENTO _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA REMOVER!")       
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            clear()
            exibir_evento(cod)
            del eventos[cod]
            print(f" EVENTO REMOVIDO COM SUCESSO! ")         
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()
    
    
#Verificar se um participantes está mat. no evento
def consultar_participante(cod, matricula): 
    if matricula in eventos[cod]['participantes']:
        return True
  
def temas_frequentes():
    cont = Counter() # Contador vazio (como um dicionário)
    for evento in eventos:
        for tema in evento['tema']:
            cont[tema] += 1 #Incrementa 1 na contagem do tema apartir do seu id
    frequentes = cont.most_common(10) # 10 temas que mais aparecem

    print("_____ TEMAS FREQUENTES _____")
    for tema, qnt in frequentes:
        print(f"{tema} - {qnt} eventos")

def participantes_mais_ativos():
    contador = Counter()  
    for evento in eventos:
        for matricula in evento['participantes']:
            contador[matricula] += 1
    mais_ativos = contador.most_common(50)

    print("_____ PARTICIPANTES MAIS ATIVOS _____")
    for matricula, qtd in mais_ativos:
        print(f"{usuarios[matricula]['nome']} - {qtd} eventos")


    

# USUÁRIOS

def criar_lista_temas(tematica):
    tema = []
    for cod in tematica:
        tema.append(temas[cod-1])
    return tema

def cadastrar_usuario():
    print("_____CADASTRO DE USUÁRIO_____")
    matricula = len(usuarios) + 1000
    nome = input("NOME COMPLETO: ")
    email = input("E-MAIL: ")

    mostrar_temas()
    tematica = input("CÓD. PREFERÊNCIAS TEMÁTICA (cód. separados por vírgula ex: 1,5,...): ")
    tematica =[tema.strip() for tema in tematica.split(",")]
    temas = criar_lista_temas(tematica)

    usuarios[matricula] = {'nome' : nome, 'email' : email, 'temas' : temas}
    return print(f'USUÁRIO {nome} CADASTRADO COM SUCESSO!')

def verificar_usuario(mat):
    if mat in usuarios:
        return True

def exibir_usuario(mat):
    print(f'''
 MATRÍCULA: {usuarios[mat]} 
 NOME: {usuarios[mat]['nome']}          
 E-MAIL: {usuarios[mat]['email']} 
 PREFERÊNCIA TEMÁTICA: {", ".join(usuarios[mat]['temas'])}

+--------------------------------------------------------------+''')

def listar_usuarios():
    print("_____ LISTAR USUÁRIOS _____")
    for mat in usuarios:
        exibir_usuario(mat)
             
def editar_evento():
    if lista_vazia(usuarios):
        print("NÃO HÁ USUÁRIOS CADASTRADOS PARA EDITAR!")
    else:
        print("_____ EDITAR USUÁRIO _____")
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
                    tematica =[tema.strip() for tema in tematica.split(",")]
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
                print("EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE!")
        continuar()

def buscar_usuario():
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
    print("_____ REMOVER PARTICIPANTE _____")
    if lista_vazia(usuarios):
        print("NÃO HÁ USUÁRIOS CADASTRADOS PARA REMOVER!")       
    else:
        mat = int(input("MATRÍCULA PARTICIPANTE: "))
        if verificar_usuario(mat):
            clear()
            exibir_usuario(mat)
            del usuarios[mat]
            print(f" USUÁRIO REMOVIDO COM SUCESSO! ")         
        else: 
            print("$# USUÁRIO NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
    continuar()


def adicionar_participante():
    print("_____ ADICIONAR PARTICIPANTE _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")       
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod)
            continuar()
            clear()
            mat = int(input("MATRÍCULA PARTICIPANTE: "))
            if verificar_usuario(mat):
                if consultar_participante(cod, mat):

                    exibir_usuario(cod)
                    continuar()
                    clear()
                    try:
                        eventos[mat]['participantes'].appens(mat)
                        print("PARTICIPANTE MATRICULADO COM SUCESSO!")
                    except:
                        print("$# NÃO FOI POSSÍVEL MATRICULAR O PARTICIPANTE! $#")
                else:
                    print("PARTICIPANTE JÁ ESTÁ MATRICULADO NESSE EVENTO!")
            else: 
                print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
            continuar()
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()