from validar import validar_opcao
from opcoes import Cadastrar

def Menu():
    print('''
          
+----------------------------+
|       MENU DE OPÇÕES       |
+----------------------------+
| 1 - Cadastrar              |
| 2 - Matricular             |
| 3 - Excluir                |
| 4 - Consultar              |    
| 5 - Relatório              |
| 0 - Sair                   |
+----------------------------+   
                                ''')
      
    opcao = validar_opcao(5)

    if opcao == 1:
        Cadastrar()

    # elif opcao == 2:
    #     Matricular()

    # elif opcao == 3:
    #     Excluir()

    # elif opcao == 4:
    #     Consultar()

    # elif opcao == 5:
    #     Relatorio()

    elif opcao == 0:
        exit()

Menu()





