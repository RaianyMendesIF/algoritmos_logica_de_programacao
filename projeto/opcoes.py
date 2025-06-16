from validar import validar_opcao
from classes.evento import cadastrar_evento, excluir_evento, consultar_evento, listar_eventos, temas_frequentes
from classes.usuario import cadastrar_usuario, excluir_usuario, consultar_usuario, listar_usuarios
from classes.participante import matricular_participante, listar_participantes, ativos_participantes

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
    matricular_participante()


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


def Relatorio(): 
    print(f'''
+--------------------------------+
|           RELATÓRIO            |
+--------------------------------+
| 1 - Eventos                    |
| 2 - Usuários                   |
| 3 - Participantes por evento   |
| 4 - Participantes mais ativos  |
| 5 - Temas mais frequentes      |
| 0 - Voltar                     |
+--------------------------------+   
                                ''')
    op = validar_opcao(5)

    if op == 1:
        listar_eventos()

    elif op == 2:
        listar_usuarios()
    
    elif op == 3:
        listar_participantes()

    elif op == 4:
        print(ativos_participantes())
        
    
    elif op == 5:
        temas_frequentes()

    elif op == 0:
        exit()
    