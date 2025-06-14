from validar import validar_opcao
from classes.evento import cadastrar_evento, excluir_evento, consultar_evento
from classes.usuario import cadastrar_usuario, excluir_usuario, consultar_usuario

def Menu2(nome):
    print(f'''
+----------------------------+
|         { nome  }          |
+----------------------------+
| 1 - Evento                 |
| 2 - Usuário                |
| 0 - Voltar                 |
+----------------------------+   
                                ''')


def Cadastrar(): 
    Menu2("CADASTRAR")
    op = validar_opcao(2)

    if op == 1:
        cadastrar_evento()        

    elif op == 2:
        cadastrar_usuario()
        
    elif op == 0:
        return


def Matricular():
    print("Não sei oq fazer ainda!")


def Excluir(): 
    Menu2(" EXCLUIR ")
    op = validar_opcao(2)

    if op == 1:
        excluir_evento()        

    elif op == 2:
        excluir_usuario()
        
    elif op == 0:
        return


def Consultar():
    Menu2("CONSULTAR")

    op = validar_opcao(2)

    if op == 1:
        consultar_evento()        

    if op == 2:
        consultar_usuario()
        
    elif op == 0:
        return


    