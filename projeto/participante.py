from evento import buscar_evento, adicionar_participante, verificar_participante, listar_todos_participantes
from usuario import buscar_usuario, nome_usuario


def matricular_participante():
    print("    MATRICULAR USUÁRIO EM EVENTO")
    event = buscar_evento()
    if event:
        print(f"EVENTO: {event[2][event[1]][0]}")
        user= buscar_usuario()
        if user:
            print(f"USUÁRIO: {user[2][user[1]][0]}")
            if verificar_participante(event[0], event[1], user[1]):
                print("\nUsuário já cadastrado no evento!")
            else:
                adicionar_participante(event[0], event[1], user[1])
                print("Usário matriculado ao evento com sucesso!")
        else:
            print("\nUsuário não identificado, verifique a matrícula e tente novamente!")
    else: 
        print("\nEvento não identificado, verifique o código e tente novamente!")


def listar_participantes():
    print("    LISTAR PARTICIPANTES POR EVENTO")
    event = buscar_evento()
    if event:
        print(f"EVENTO: {event[2][event[1]][0]}")
        participantes = event[2][event[1]][3]
        for i,matricula in enumerate(participantes):
            print(f"{i+1} - {nome_usuario(matricula)}")

    else: 
        print("\nEvento não identificado, verifique o código e tente novamente!")
    

def ativos_participantes():
    participantes = listar_todos_participantes()
    unicos = set(participantes)
    frequencia = []
    for user in unicos:
        ativo = participantes.count(user)
        frequencia.append([user, ativo])
    frequencia = ordenar_lista_maior(frequencia,1)

    print("   USUÁRIO                       CURSOS MAT.")
    for user in frequencia:
        print(f"{nome_usuario(user[0])}         {user[1]} curso(s)")
   

def ordenar_lista_maior(lista,item): #  Bubble Sort
    tam = len(lista)
    for i in range(tam):
        for j in range(tam - i - 1):
            if lista[j][item] < lista[j + 1][item]:    
                lista[j][item], lista[j + 1][item] = lista[j + 1][item], lista[j][item]
    return lista
        
            