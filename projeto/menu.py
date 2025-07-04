from utilidades import validar_opcao, clear
from opcoes import Eventos, Participantes

def Menu():
    print('''
       COMUNIDADE TECH    
+----------------------------+
|       MENU DE OPÇÕES       |
+----------------------------+
| 1 - EVENTOS                |
| 2 - PARTICIPANTES          |
| 0 - ENCERRAR SESSÃO        |
+----------------------------+   
                                ''')
      
    opcao = validar_opcao(2)
    clear()
    
    if opcao == 1:
        Eventos()

    elif opcao == 2:
        Participantes()

    elif opcao == 0:
        print("SESSÃO ENCERRADA!")
        exit()






