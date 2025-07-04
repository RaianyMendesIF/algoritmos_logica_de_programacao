from functools import reduce
from participante_evento import listar_participantes
from utilidades import validar_opcao, clear, continuar, lista_vazia, titulo


eventos = { 1: {'tipo' : 'Maratona de Programação', 'nome' : 'Programação em Python', 'max_participantes': 20, 'data' : '25/08/2025','hora' : '15:30','duracao' : '5h 45min',
            'local' : 'IFMS - Campus Três Lagoas', 'tema' : 'Linguagens de Programação', 'palestrante' : 'Rogério Antoniassi', 'qnt_participantes' : 3, 'participantes' : [1002, 1001, 1000]},
            2: {'tipo' : 'Workshop', 'nome' : 'Cybersegurança', 'max_participantes': 15, 'data' : '14/09/2025','hora' : '16:40','duracao' : '1h 45min',
            'local' : 'IFMS - Campus Três Lagoas', 'tema' : 'Segurança', 'palestrante' : 'Evandro Rocha', 'qnt_participantes' : 2, 'participantes' : [1002, 1001]},
            3: {'tipo' : 'Minicurso', 'nome' : 'MySQL', 'max_participantes': 20, 'data' : '19/07/2025','hora' : '14:45','duracao' : '1h 15min',
            'local' : 'IFMS - Campus Três Lagoas', 'tema' : 'Banco de Dados', 'palestrante' : 'Maraisa Guerra', 'qnt_participantes' : 1, 'participantes' : [1000]}, } 

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

# Temas  
def listar_temas():
    print("TEMA")
    for i,tema in enumerate(temas):
        print(f'{i+1} - {tema}')
    print("0 - Adicionar tema")

def adicionar_tema(novo_tema):
    temas.append(novo_tema)
    return len(temas)

#Ttpos de eventos
def listar_tipos_evento():
    print("TIPO DE EVENTO ")
    for i,tipo in enumerate(tipos_evento):
        print(f'{i+1} - {tipo}')
    print("")

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
   
def verificar_evento(cod):
    if cod in eventos:
        return eventos[cod]
