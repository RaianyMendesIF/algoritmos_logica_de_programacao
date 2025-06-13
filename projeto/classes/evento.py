eventos = []

def cadastrar_evento():
    print("_____CADASTRO DE EVENTO_____")
    cod = len(eventos) + 1
    nome = input("NOME: ")
    data = input("DATA(xx/xx/xxxx): ")
    tema = input("TEMA: ")
    eventos.append({cod:[nome, data, tema]})

    return print(f'{nome} cadastrado(a) com sucesso!')

def listar_evento():
    for i in eventos.items():
        print(i)
