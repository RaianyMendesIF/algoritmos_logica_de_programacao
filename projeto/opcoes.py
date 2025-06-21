from utilidades import validar_opcao, clear
from funcoes import cadastrar_evento, listar_eventos, editar_evento, buscar_evento, remover_evento, adicionar_participante
from funcoes import cadastrar_usuario, listar_usuarios, editar_usuario, buscar_usuario, remover_usuario

def Menu2(nome, nova):
    clear()
    print(f'''
+-----------------------------+
|       {    nome   }         |
+-----------------------------+
| 1 - CADASTAR                |
| 2 - LISTAR                  |
| 3 - EDITAR                  |
| 4 - BUSCAR                  |    
| 5 - EXCLUIR                 |
| 6 - {           nova       }|
| 0 - VOLTAR                  |
+-----------------------------+   ''')

def Eventos(): 
    while True:
        Menu2("   EVENTO   ", " ADICIONAR PARTICIPANTE")
        op = validar_opcao(5)
        clear()
        if op == 1:
            cadastrar_evento() 

        elif op == 2:
            listar_eventos()

        elif op == 3:
            editar_evento()

        elif op == 4:
            buscar_evento()

        elif op == 5:
            remover_evento()

        elif op == 6:
            adicionar_participante()
        elif op == 0:
            return

def Participantes():
    while True:
        Menu2("PARTICIPANTE", "MATRICULAR             ")

        op = validar_opcao(5)
        clear()
        if op == 1:
            cadastrar_usuario() 

        elif op == 2:
            listar_usuarios()

        elif op == 3:
            editar_usuario()

        elif op == 4:
            buscar_usuario()

        elif op == 5:
            remover_usuario()

        elif op == 6:
            adicionar_participante()
            
        elif op == 0:
            return
        
def Relatorios():
    while True:
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
            clear()
        

        elif op == 4:
            clear()
            
            
        
        elif op == 5:
            clear()

        elif op == 0:
            exit()
    