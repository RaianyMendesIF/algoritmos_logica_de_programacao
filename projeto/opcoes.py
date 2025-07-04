from utilidades import validar_opcao, clear, confirmar_gerarPDF, continuar, titulo, lista_vazia, sair, confirmar_exclusao
from usuario import usuarios, listar_usuarios, verificar_usuario, exibir_usuario, temas_usuario
from participante_evento import remover_usuario_cursos
from evento import eventos,


from funcoes import cadastrar_evento, listar_eventos, editar_evento, buscar_evento, remover_evento, temas_frequentes, verificar_evento
from funcoes import cadastrar_usuario, listar_usuarios, editar_usuario, buscar_usuario, remover_usuario
from funcoes import adicionar_participante, remover_participante, listar_participantes_evento, participantes_mais_ativos
from funcoes import exportar_lista_eventos, exportar_lista_usuarios, exportar_participante_evento, exportar_participante_ativo,exportar_temas_frequente
from funcoes import verificar_usuarios, verificar_eventos
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
            global usuarios
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
                            except:
                                print("$# NÃO FOI POSSÍVEL REMOVER O PARTICIPANTE! $#")
                                continuar() 
                                return 
                            try: 
                                remover_usuario(mat)  
                                print(f" USUÁRIO REMOVIDO COM SUCESSO! ")
                                continuar()
                                return
                            except:
                                print("$#ERRO AO REMOVER O PARTICIPANTE! $#")
                                continuar()            
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
            print("_____ ADICIONAR PARTICIPANTE _____")
            if lista_vazia(eventos):
                print("NÃO HÁ EVENTOS CADASTRADOS PARA ADICIONAR PARTICIPANTE!")    
                continuar()   
            else:
                cod = int(input("CÓDIGO EVENTO: "))
                if verificar_evento(cod):
                    exibir_evento(cod)
                    continuar()
                    clear()
                    if lista_vazia(usuarios):
                        print("NÃO HÁ USUÁRIOS CADASTRADOS PARA ADICIONAR!")    
                        continuar()   
                    else:
                        mat = int(input("MATRÍCULA PARTICIPANTE: "))
                        if verificar_usuario(mat):
                            if consultar_participante(cod, mat):
                                print("PARTICIPANTE JÁ ESTÁ MATRICULADO NESSE EVENTO!")
                            else:
                                exibir_usuario(mat)
                                continuar()
                                clear()
                                adicionar_participante()
                                return
                        else:
                            print("$# PARTICIPANTE NÃO IDENTIFICADO, VERIFIQUE A MATRÍCULA E TENTE NOVAMENTE! $#")
                        continuar()
                else: 
                    print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
                    continuar()

            

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
                if verificar_eventos():
                    if confirmar_gerarPDF():
                        nome = input("NOME DO ARQUIVO:")
                        nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                        exportar_lista_eventos(nome)
                        continuar() 
                      

        elif op == 2:
            listar_usuarios()
            if verificar_usuarios():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_lista_usuarios(nome)
                    continuar()

              
        elif op == 3:
            listar_participantes_evento()
            if verificar_eventos():
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
            if verificar_usuarios():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_participante_ativo(nome)
                    continuar()
                   
        elif op == 5:
            
            temas_frequentes()
            if verificar_eventos():
                if confirmar_gerarPDF():
                    nome = input("NOME DO ARQUIVO: ")
                    nome = nome.replace(" ", "").replace(".", "") + ".pdf"
                    exportar_temas_frequente(nome)
                    continuar()

        elif op == 0:
            return
    