import os

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