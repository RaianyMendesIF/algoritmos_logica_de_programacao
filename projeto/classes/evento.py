
eventos = [{1: ['Introdução a Tecnologia', '25/07/2025', 'Novas tecnologias de mercado',[1000, 1001]]}, {2: ['Tecnologia', '15/08/2025', 'Algoritmo',[1000]]}] #

def cadastrar_evento():
    print("_____CADASTRO DE EVENTO_____")
    cod = len(eventos) + 1
    nome = input("NOME: ")
    data = input("DATA(xx/xx/xxxx): ")
    tema = input("TEMA: ")
    eventos.append({cod:[nome, data, tema,[]]})

    return print(f'Evento {nome} cadastrado(a) com sucesso!')


def listar_eventos():
    print('''\n             EVENTOS''', end='')
    for evento in eventos:
        for i in evento.keys():
            print(f'''
+-------------------------------+
                  
 COD: {i} | NOME: {evento[i][0]}          
 DATA: {evento[i][1]} | TEMA: {evento[i][2]}              
 PARTICIPANTES: {evento[i][3]} ''')
    print("\n+-------------------------------+")


def lista_vazia_eventos():
     if len(eventos) == 0:
          return True
     

def buscar_evento():
    if lista_vazia_eventos():
        print("\nNão há eventos cadastrados!")
        
    else:
        listar_eventos()
        cod = int(input("CÓDIGO EVENTO: "))

        for evento in eventos:
            for i, key in enumerate(evento.keys()):
                if key == cod:
                    return i, key, evento
        return 
        

def excluir_evento():
    print("    EXLUIR EVENTO")
    evento = buscar_evento()

    if evento:
        eventos.remove(evento[2])
        print(f"\nEvento {evento[2][evento[1]][0]} excluído com sucesso!")
    else:
        print("\nCurso não identificado, verifique o código e tente novamente!")


def consultar_evento():
    print("    CONSULTAR EVENTO")
    event = buscar_evento()
    if event:
        print(f'''
+-------------------------------+
                    
 COD: {event[1]} | NOME: {event[2][event[1]][0]}          
 DATA: {event[2][event[1]][1]} | TEMA: {event[2][event[1]][2]}
 PARTICIPANTES: {event[2][event[1]][3]}''')
        print("\n+-------------------------------+")

    else:
        print("\nEvento não identificado, verifique o código e tente novamente!")
    

def listar_todos_participantes():
    participantes = []
    for evento in eventos:
        for key in evento.keys():
            participantes += evento[key][3]
    return participantes


def adicionar_participante(indice, key, matricula):
    participantes = eventos[indice][key][3]
    participantes.append(matricula)


def verificar_participante(indice, key, matricula):
    participantes = eventos[indice][key][3]
    if matricula in participantes:
        return True
    

def temas_frequentes():

    temas = []
    for evento in eventos:
        for key in evento.keys():
           temas.append(evento[key][2]) 
    print("     TEMAS FREQUENTES")
    for tema in temas:
        print(tema, '-', temas.count(tema), 'curso(S)')