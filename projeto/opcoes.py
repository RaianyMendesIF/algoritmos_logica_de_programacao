from validar import validar_opcao
from classes.evento import cadastrar_evento, listar_evento
from classes.usuario import cadastrar_usuario, listar_usuario

def Cadastrar(): 
    print(f'''
+----------------------------+
|         CADASTRAR          |
+----------------------------+
| 1 - Evento                 |
| 2 - Usuário                |
| 0 - Voltar                 |
+----------------------------+   
                                ''')
    op = validar_opcao(2)

    if op == 1:
        cadastrar_evento()
        listar_evento()
    elif op == 2:
        cadastrar_usuario()
        listar_usuario()
        
    elif op == 0:
        exit()


