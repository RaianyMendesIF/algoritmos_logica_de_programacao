from utilidades import validar_opcao, clear
from opcoes import Eventos, Participantes, Relatorios

def Menu():
    print('''
       COMUNIDADE TECH    
+----------------------------+
|       MENU DE OPÇÕES       |
+----------------------------+
| 1 - EVENTOS                |
| 2 - PARTICIPANTES          |
| 3 - RELATÓRIOS             |
| 0 - ENCERRAR SESSÃO        |
+----------------------------+   
                                ''')
      
    opcao = validar_opcao(3)
    clear()
    
    if opcao == 1:
        Eventos()

    elif opcao == 2:
        Participantes()

    elif opcao == 3:
        Relatorios()

    elif opcao == 0:
        print("SESSÃO ENCERRADA!")
        exit()






