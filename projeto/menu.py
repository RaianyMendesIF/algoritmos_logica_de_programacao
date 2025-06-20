from utilidades import validar_opcao, clear
from opcoes import Eventos, Participantes, Relatorios 

def Menu():
    print('''
          
+----------------------------+
|       MENU DE OPÇÕES       |
+----------------------------+
| 1 - EVENTOS                |
| 2 - PARTICIPANTES          |
| 3 - RELATÓRIO              |
| 0 - SAIR                   |
+----------------------------+   
                                ''')
      
    opcao = validar_opcao(6)
    clear()
    
    if opcao == 1:
        Eventos()

    elif opcao == 2:
        Participantes()

    elif opcao == 3:
        Relatorios()

    elif opcao == 0:
        exit()






