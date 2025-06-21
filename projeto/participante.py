from evento import buscar_evento, adicionar_participante, verificar_participante, listar_todos_participantes
from usuario import buscar_usuario, nome_usuario



    

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
        
            