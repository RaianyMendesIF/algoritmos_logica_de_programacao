usuarios = []

def cadastrar_usuario():
    print("_____CADASTRO DE USUÁRIO_____")
    matricula = len(usuarios) + 1000
    nome = input("NOME COMPLETO: ")
    email = input("E-MAIL: ")
    preferencia_tematica = input("PREFERÊNCIA TEMÁTICA: ")
    usuarios.append({matricula:[nome, email, preferencia_tematica]})

    return print(f'{nome} cadastrado(a) com sucesso!')

def listar_usuario():
    for i in usuarios.items():
        print(i)