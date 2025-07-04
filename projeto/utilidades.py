import os
# validar_opcao, clear, continuar, lista_vazia, sair, confirmar_gerarPDF, titulo, confirmar_exclusao

def validar_opcao(maximo, minimo=0):
    while True:
        try:     # O bloco try é o código que pode causar um erro. 
            op = int(input("OPÇÃO: "))
            if minimo <= op <= maximo:
                return op
            else:
                print("Opção inválida, tente novamente!")

        except ValueError: # Se houver um erro, o except informar sobre o problema no caso de argumento do tipo incorreto.
            print("Entrada inválida, digite um número.")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input("\nDigite enter para continuar...")
    clear()

def lista_vazia(lista):  
    if len(lista) == 0:
          return True
    
def sair(nome_secao):
    sair = input("\nDESEJA SAIR DA SEÇÃO?(S/N): ")
    if sair.upper() == 'S':
        print(f"Saindo da seção {nome_secao}")
        return True
    else:
        return False

def confirmar_gerarPDF():
    op = input("DESEJA EXPORTAR O RELATÓRIO EM PDF?(S/N) ")
    if op.upper() == "S":
        clear()
        return True

def titulo(texto):
    print(f"------------------------- {texto} -------------------------")

def confirmar_exclusao():
    op = input("CONFIRMAR EXCLUSÃO(S/N): ")
    if op.upper() == "S":
        return True
    