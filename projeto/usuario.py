usuarios = {1000 : {'nome' : 'Raiany Mendes', 'email' : 'raiany@gmail.com', 'temas' : ['Segurança', 'Análise de Dados'], 'eventos' : [1 , 3]},
            1001 : {'nome' : 'Sara Mendes', 'email' : 'sara@gmail.com', 'temas' : ['Análise de Dados', 'Banco de Dados',], 'eventos' : [1 , 2]},
            1002 : {'nome' : 'Yasmin Silva', 'email' : 'yasmin@gmail.com', 'temas' : ['Análise de Dados', 'Segurança',], 'eventos' : [1 , 2]}}

from evento import mostrar_temas, temas
from participante_evento import listar_eventos_matriculado
from utilidades import validar_opcao, clear, continuar, lista_vazia, titulo
from functools import reduce


def gerar_id_usuario():
    tam = len(usuarios)
    if tam == 0:
        return tam + 1000
    else:
        ultimo_id = reduce(lambda x, y: x if x > y else y, usuarios.keys())
        return ultimo_id + 1

# Cadastrar um usuário
def cadastrar_usuario(nome, email, tematicas):
    try:
        matricula = gerar_id_usuario()
        usuarios[matricula] = {'nome' : nome, 'email' : email, 'temas' : tematicas, 'eventos' : []}
        print(f'PARTICIPANTES {nome} CADASTRADO COM SUCESSO! \nID: {matricula}')
    except TypeError:
        print("%$ NÃO FOI POSSÍVEL REALIZAR O CADASTRO, VERIFIQUE OS DADOS E TENTE NOVAMENTE! $%")
    continuar()

# Laço para adicionar vários temas de preferência do usuário
def temas_usuario():
    tematicas = []
    op = 'S'
    while op.upper() == 'S':
        tema = selecionar_tema()
        if tematicas.index(tema):
            print("CURSO JÁ ADICIONADO!")
        else:
            tematicas.append(tema)
            [print("TEMAS: ",i, end='; ') for i in tematicas]
        op = input("\nDESEJA ADICIONAR MAIS TEMAS?:(S/N)")
        clear()
    return tematicas

# Mostrar e validar a escolha de um tem ou adicionar
def selecionar_tema():
    mostrar_temas()
    op = validar_opcao(len(temas))

    if op == 0:
        clear()
        novo_tema = input("NOVO TEMA: ")
        op = adicionar_tema(novo_tema)

    return temas[op-1]

# Adicionar um tema 
def adicionar_tema(novo_tema):
    temas.append(novo_tema)
    return len(temas)

# Listar todos os usuários cadastrados
def listar_usuarios():
    titulo("LISTAR PARTICIPANTES")
    if lista_vazia(usuarios):
        print("NÃO HÁ PARTICIPANTES CADASTRADOS PARA LISTAR!")   
    else:
        for mat in usuarios:
            exibir_usuario(mat)
    continuar()

#Exibir as informações do usuário pela matricula, determinando o nível de inf.
def exibir_usuario(mat, event=False):
    print(f'''
 MATRÍCULA: {mat}   |   NOME: {usuarios[mat]['nome']}          
 E-MAIL: {usuarios[mat]['email']} 
 PREFERÊNCIA TEMÁTICA: {", ".join(usuarios[mat]['temas'])}
''')
 
    if event == True:
        listar_eventos_matriculado(mat)

    print('+----------------------------------------------------------------------------------------------------+')

# Verificar se a matricula do usuário existe
def verificar_usuario(mat):
    if mat in usuarios:
        return True
    
def editar_usuario(mat):
    while True:    
        exibir_usuario(mat)
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
                usuarios[mat]['email'] = email 
                print(f"EMAIL ALTERADO PARA {email} COM SUCESSO!")
            except:
                print("$@ NÃO FOI POSSÍVEL ALTERAR O EMAIL DO PARTICIPANTE! @$")
            continuar()

            if op == 3:
                print("_____ EDITAR PREFERÊNCIA TEMÁTICA _____")
                tematicas = temas_usuario()

                try:
                    usuarios[mat]['temas'] = tematicas 
                    print(f"PREFERÊNCIA TEMÁTICA ALTERADA COM SUCESSO!")
                except:
                    print("$@ NÃO FOI POSSÍVEL ALTERAR A PREFERÊNCIA TEMÁTICA DO PARTICIPANTE! @$")
                continuar()

            if op == 0:
                return

        continuar()

def remover_usuario(mat):
    del usuarios[mat]

