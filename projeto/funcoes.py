from evento import eventos, tipos_evento, temas
from usuario import usuarios
from utilidades import validar_opcao, lista_vazia, clear, continuar
from collections import Counter #  contar a frequência de elementos em uma sequência

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
        op = adicionar_tema()

    return temas[op-1]

def adicionar_tema():
    novo_tema = input("NOVO TEMA:")
    temas.append(novo_tema)
    return len(temas)-1

#EVENTOS
def cadastrar_evento():
    print("_____ CADASTRO DE EVENTO _____")
    cod = len(eventos) + 1
    nome = input("NOME: ")

    #TIPO EVENTO
    mostrar_tipos_evento()
    op = validar_opcao(4)
    tipo = tipos_evento[op-1]

    data = input("DATA(xx/xx/xxxx): ")

    # TEMA EVENTO
    mostrar_temas()
    op = validar_opcao(len(temas)-1)
    if op == 0:
      op = adicionar_tema()
    tema = temas[op-1]

    eventos[cod] = {'nome' : nome, 'tipo' : tipo, 'data' : data, 'tema' : tema, 'participantes' : []}
    clear()
    print(f'Evento {nome} cadastrado(a) com sucesso!')
    continuar()

def verificar_evento(cod):
    if cod in eventos:
        return True

def exibir_evento(k):
    print(f'''
 COD: {k} | NOME: {eventos[k]['nome']} | TIPO: {eventos[k]['tipo']}      
 DATA: {eventos[k]['data']} | TEMA: {eventos[k]['tema']}              
 PARTICIPANTES: {eventos[k]['participantes']} 

+--------------------------------------------------------------+''')

def listar_eventos():
    print("_____ LISTAR EVENTOS _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA LISTAR!")   
    else:
        for key in eventos.keys():
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
                    op = validar_opcao(4)
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
                    tam = len(temas)-1
                    op = validar_opcao(tam)
                    clear()
                    if op == 0:
                        op = adicionar_tema() 
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
        
def excluir_evento():
    print("_____ EXCLUIR EVENTO _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod)
            eventos = [evento for evento in eventos if evento != eventos[cod]] 
            print(f"EVENTO {eventos[cod]['nome']} EXCLUÍDO COM SUCESSO!")
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()

def adicionar_participante(key, matricula):
    print("_____ ADICIONAR PARTICIPANTE _____")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")       
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            exibir_evento(cod)
            eventos[key]['participantes'].append(matricula)
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()
    

#Verificar se um participantes está mat. no evento
def consultar_participante(key, matricula): 
    if matricula in eventos[key]['participantes']:
        return True
  
def temas_frequentes():
    cont = Counter() # Contador vazio (como um dicionário)
    for evento in eventos:
        for tema in evento['tema']:
            cont[tema] += 1 #Incrementa 1 na contagem do tema apartir do seu id
    frequentes = cont.most_common(10) # 10 temas que mais aparecem

    print("_____ 10 TEMAS FREQUENTES _____")
    for tema, qnt in frequentes:
        print(f"{tema} - {qnt} eventos")