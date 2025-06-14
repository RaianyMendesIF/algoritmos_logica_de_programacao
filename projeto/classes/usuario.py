usuarios = [{1000: ['Raiany Vitoria P. Mendes', 'raiany@gmail.com', 'IA e Lógica de programação']}]

def cadastrar_usuario():
    print("_____CADASTRO DE USUÁRIO_____")
    matricula = len(usuarios) + 1000
    nome = input("NOME COMPLETO: ")
    email = input("E-MAIL: ")
    preferencia_tematica = input("PREFERÊNCIA TEMÁTICA: ")
    usuarios.append({matricula:[nome, email, preferencia_tematica]})
    return print(f'Usuário {nome} cadastrado(a) com sucesso!')


def listar_usuario():
    print('''\n             USUARIOS''', end='')
    for user in usuarios:
        for i in user.keys():
             print(f'''
+-------------------------------+
                  
 MATRÍCULA: {i} 
 NOME: {user[i][0]}          
 E-MAIL: {user[i][1]} 
 PREFERÊNCIA TEMÁTICA: {user[i][2]}''')
    print("\n+-------------------------------+")


def lista_vazia(lista):
     if len(lista) == 0:
          return True


def buscar_usuario():
    if lista_vazia(usuarios):
             print("\nNão há usuários cadastrados!")
    else:
        listar_usuario()
        matricula = int(input("MATRÍCULA: "))

        for user in usuarios:
            for i,key in enumerate(user.keys()):
                if key == matricula:
                    return i, key, user
        return 
                

def excluir_usuario():
    user = buscar_usuario()

    if user:
        usuarios.remove(user[2])
        print(f"\nUsuário {user[2][user[1]][0]} excluído com sucesso!")
    else:
        print("\nUsuário não identificado, verifique a matrícula e tente novamente!")


def consultar_usuario():
    user = buscar_usuario()
    if user:
        print(f'''
+-------------------------------+
                    
 MATRÍCULA: {user[1]} 
 NOME: {user[2][user[1]][0]}          
 E-MAIL: {user[2][user[1]][1]} 
 PREFERÊNCIA TEMÁTICA: {user[2][user[1]][2]}''')
        print("\n+-------------------------------+")
    else:
        print("\nUsuário não identificado, verifique a matrícula e tente novamente!")


