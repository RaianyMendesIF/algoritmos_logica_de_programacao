from utilidades import validar_opcao, clear, confirmar_gerarPDF, continuar
from funcoes import cadastrar_evento, listar_eventos, editar_evento, buscar_evento, remover_evento, temas_frequentes, verificar_evento
from funcoes import cadastrar_usuario, listar_usuarios, editar_usuario, buscar_usuario, remover_usuario
from funcoes import adicionar_participante, remover_participante, listar_participantes_evento, participantes_mais_ativos
from funcoes import exportar_lista_eventos, exportar_lista_usuarios, exportar_participante_evento, exportar_participante_ativo,exportar_temas_frequente

def Menu2(nome, nova, nova2):
    clear()
    print(f'''
+-----------------------------+
|       {    nome   }         |
+-----------------------------+
| 1 - CADASTRAR               |
| 2 - LISTAR                  |
| 3 - EDITAR                  |
| 4 - BUSCAR                  |    
| 5 - EXCLUIR                 |
| 6 - {           nova       }|
| 7 - {           nova2      }|
| 0 - VOLTAR                  |
+-----------------------------+   ''')

def Eventos(): 
    while True:
        Menu2("   EVENTO    ", "ADICIONAR PARTICIPANTE  ", "REMOVER PARTICIPANTE    " )
        
        op = validar_opcao(7)
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

        elif op == 7:
            remover_participante()
        
        elif op == 0:
            return

def Participantes():
    while True:
        Menu2("PARTICIPANTE", "MATRICULAR PARTICIPANTE ", "REMOVER PARTICIPANTE    ")

        op = validar_opcao(7)
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

        elif op == 7:
            remover_participante()
            
        elif op == 0:
            return
        
def Relatorios():
    while True:
        print(f'''
    +--------------------------------+
    |           RELATÓRIO            |
    +--------------------------------+
    | 1 - EVENTOS                    |
    | 2 - USUÁRIOS                   |
    | 3 - PARTICIPANTES POR EVENTO   |
    | 4 - PARTICIPANTES MAIS ATIVOS  |
    | 5 - TEMAS MAIS FREQUENTES      |
    | 0 - VOLTAR                     |
    +--------------------------------+   
                                    ''')
        op = validar_opcao(5)
        clear()

        if op == 1:
            listar_eventos()
            if confirmar_gerarPDF():
                nome = input("NOME DO ARQUIVO:")
                nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                exportar_lista_eventos(nome)
                continuar()
            else:
                return

        elif op == 2:
            listar_usuarios()
            if confirmar_gerarPDF():
                nome = input("NOME DO ARQUIVO: ")
                nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                exportar_lista_usuarios(nome)
                continuar()
            else:
                return
              
        elif op == 3:
                cod = int(input("CÓDIGO EVENTO: "))
                if verificar_evento(cod):
                    if confirmar_gerarPDF():
                        nome = input("NOME DO ARQUIVO: ")
                        nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                        exportar_participante_evento(nome, cod)
                        continuar()
                    else:
                        return
                else:
                    print("EVENTO NÃO IDENTIFICADO! REVEJA O CÓDIGO E TENTE NOVAMENTE!")
                    return
        
        elif op == 4:
            if confirmar_gerarPDF():
                nome = input("NOME DO ARQUIVO: ")
                nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                exportar_participante_ativo(nome)
                continuar()
            else:
                return
            
                 
        elif op == 5:
            if confirmar_gerarPDF():
                nome = input("NOME DO ARQUIVO: ")
                nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                exportar_temas_frequente(nome)
                continuar()
            else:
                return

        elif op == 0:
            return
    