from utilidades import validar_opcao, clear, continuar, lista_vazia, sair, confirmar_exclusao, titulo, confirmar_gerarPDF
from funcoes_evento import temas, tipos_evento, listar_tipos_evento, listar_temas, adicionar_tema
from funcoes_evento import  cadastrar_evento, exibir_evento, listar_eventos, editar_evento, remover_evento, verificar_evento
from funcoes_tema import adicionar_tema
from funcoes_usuario import cadastrar_usuario, listar_usuarios, exibir_usuario, verificar_usuario, editar_usuario, remover_usuario, temas_usuario
from funcoes_evento import adicionar_participante, remover_participante
from funcoes_evento import remover_usuario_cursos, remover_evento_usuarios, remover_participante
from relatorio import listar_participantes_evento, temas_frequentes, participantes_mais_ativos
from relatorio import exportar_lista_eventos, exportar_lista_usuarios, exportar_participante_ativo, exportar_participante_evento, exportar_temas_frequente

from dados.eventos import eventos
from dados.usuarios import usuarios


def Menu2(nome):
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
| 6 - MATRICULAR PARTICIPANTE |
| 7 - REMOVER PARTICIPANTE    |
| 0 - VOLTAR                  |
+-----------------------------+   ''')

def Eventos(): 
    while True:
        Menu2("   EVENTO    ")
        
        op = validar_opcao(7)
        clear()

        if op == 1:
            titulo("CADASTRO DE EVENTO")
                       
            #TIPO EVENTO
            listar_tipos_evento()
            op = validar_opcao(4, 1)
            tipo = tipos_evento[op-1]
            
            nome = input("NOME: ")
            palestrante = input("PALESTRANTE: ")
            max_parti = input("TOTAL PARTICIPANTES: ")
            data = input("DATA(xx/xx/xxxx): ")
            horario = input("HORÁRIO: ")
            duracao = input("DURAÇÃO: ")
            local = input("LOCAL: ")
            

            # TEMA EVENTO
            listar_temas()
            op = validar_opcao(len(temas))
            if op == 0:
                novo_tema = input("NOVO TEMA:")
                op = adicionar_tema(novo_tema) 
                tema = temas[op-1]
            
            cadastrar_evento(tipo, nome, palestrante, max_parti, data, horario, duracao, local, tema) 


        elif op == 2:
            listar_eventos()


        elif op == 3:
            if lista_vazia(eventos):
                titulo("EDITAR EVENTOS")
                print("NÃO HÁ EVENTOS CADASTRADOS PARA EDITAR!")
            else:
                titulo("EDITAR EVENTO")
                cod = int(input("CÓD. EVENTO: "))
                if verificar_evento(cod):
                    exibir_evento(cod) 
                    continuar() 
                    editar_evento(cod)
                else:
                    print("EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE!")

           

        elif op == 4:
            while True:
                titulo("BUSCAR EVENTO")
                if lista_vazia(eventos):
                    print("NÃO HÁ EVENTOS CADASTRADOS PARA BUSCAR!")
                    continuar()   
                    return    
                else:
                    cod = int(input("CÓDIGO EVENTO: "))
                    if verificar_evento(cod):
                        exibir_evento(cod, True)
                        if sair("BUSCAR EVENTO") == True:
                            return
                        else:
                            clear()
                    else: 
                        print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
                        if sair("BUSCAR EVENTO") == True:
                            return
                        else: 
                            clear( )

        elif op == 5:
            while True:
                titulo("REMOVER EVENTO")
                if lista_vazia(eventos):
                    print("NÃO HÁ EVENTOS CADASTRADOS PARA REMOVER!")
                    continuar() 
                    return 
                else:
                    cod = int(input("CÓDIGO EVENTO: "))
                    if verificar_evento(cod):
                        clear()
                        titulo("REMOVER EVENTO")
                        exibir_evento(cod)
                        conf = confirmar_exclusao()
                        if conf:
                            try:  
                                remover_evento_usuarios(cod)
                                remover_evento(cod)
                                print(f" EVENTO REMOVIDO COM SUCESSO! ")
                                continuar()
                            except:
                                print("$#ERRO AO REMOVER O PARTICIPANTE! $#") 
                                continuar()   
                        else:
                            print(f"OPERAÇÃO DE EXCLUSÃO CANCELADA! ")
                            continuar()       
                    else: 
                        print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
                        continuar()

                if sair("REMOVER EVENTO") == True:
                    return
                else:
                    clear()
                    remover_evento()

        elif op == 6:
            adicionar_participante()

        elif op == 7:
            remover_participante()
        
        elif op == 0:
            return

def Participantes():
    while True:
        Menu2("PARTICIPANTES")

        op = validar_opcao(7)
        clear()

        if op == 1:
            titulo("CADASTRO DE USUÁRIO")
            nome = input("NOME COMPLETO: ")
            email = input("E-MAIL: ")

            tematicas = temas_usuario()
            
            cadastrar_usuario(nome, email, tematicas)
                
        elif op == 2:
            listar_usuarios()

        elif op == 3:
            titulo("EDITAR USUÁRIO")
            if lista_vazia(usuarios):
                print("NÃO HÁ USUÁRIOS CADASTRADOS PARA EDITAR!")
                continuar()
            else:
                mat = input("MATRÍCULA USUÁRIO: ")
                if verificar_usuario(mat):
                        exibir_usuario(mat)
                        continuar()
                        editar_usuario(mat)
                else:
                    print("USUÁRIO NÃO ENCONTRADO, VERIFIQUE O ID E BUSQUE NOVAMENTE!")
                    continuar()
      
        elif op == 4:
            if lista_vazia(usuarios):
                    titulo("BUSCAR USUÁRIO")
                    print("NÃO HÁ USUÁRIOS CADASTRADOS PARA BUSCAR!")
            else:
                while True:
                    titulo("BUSCAR USUÁRIO")
                    matricula = int(input("MATRÍCULA USUÁRIO: "))
                    if matricula in usuarios:
                        exibir_usuario(matricula, True)
                    else:
                        print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! #$")
                        continuar()
                    if sair("BUSCAR EVENTO") == True:
                            return
                    else:
                        clear()

        elif op == 5:
            titulo("REMOVER PARTICIPANTE")
            while True:
                if lista_vazia(usuarios):
                    print("NÃO HÁ USUÁRIOS CADASTRADOS PARA REMOVER!")
                    continuar()
                    return      
                else:
                    mat = int(input("MATRÍCULA PARTICIPANTE: "))
                    if verificar_usuario(mat):
                        clear()
                        exibir_usuario(mat)
                        conf = confirmar_exclusao()
                        if conf:
                            try: # remover a mat das listas do curso
                                cursos = usuarios[mat]['eventos']
                                remover_usuario_cursos(cursos, mat)
                                remover_usuario(mat)  
                                print(f" USUÁRIO REMOVIDO COM SUCESSO! ")
                                continuar()
                            except:
                                print("$# NÃO FOI POSSÍVEL REMOVER O PARTICIPANTE! $#")
                                continuar() 
                                return            
                        else:
                            print(f"OPERAÇÃO DE EXCLUSÃO CANCELADA! ")
                            continuar()    
                    else: 
                        print("$# USUÁRIO NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
                        continuar()

                if sair("REMOVER EVENTO") == True:
                    return
                else:
                    clear()

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
                continuar()
                if verificar_evento():
                    if confirmar_gerarPDF():
                        nome = input("NOME DO ARQUIVO:")
                        nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                        exportar_lista_eventos(nome)
                        continuar() 
                      

        elif op == 2:
            listar_usuarios()
            continuar()
            if verificar_usuario():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_lista_usuarios(nome)
                    continuar()

              
        elif op == 3:
            listar_participantes_evento()
            continuar()
            if verificar_evento():
                if confirmar_gerarPDF() :
                    cod = int(input("CÓDIGO EVENTO: "))
                    if verificar_evento(cod):
                        nome = input("NOME DO ARQUIVO: ")
                        nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                        exportar_participante_evento(nome, cod)
                        continuar()
                    else:
                        print("EVENTO NÃO IDENTIFICADO! REVEJA O CÓDIGO E TENTE NOVAMENTE!")
            
        
        elif op == 4:
            participantes_mais_ativos()
            continuar()
            if verificar_usuario():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_participante_ativo(nome)
                    continuar()
                   
        elif op == 5:
            temas_frequentes()
            continuar()
            if verificar_evento():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_temas_frequente(nome)
                    continuar()

        elif op == 0:
            return
    