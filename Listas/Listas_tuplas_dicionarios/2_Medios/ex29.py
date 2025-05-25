#  Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.

lista = []

def menu(): 
    print("""
_______MENU_______

A - Adicionar
R - Remover
L - Listar itens
E - Sair da lista
""")
    
def adicionar(item):
    lista.append(item)

def remover(item):
    lista.remove(item)


def mostra_lista():
    print("\n\n__________ITENS__________\n")
    for i, item in enumerate(lista):
        print(f"{i+1} - {item}")
    print("\n_________________________\n\n")

def main():
    while True:
        menu()
        atv = input("Digite a atividade desejada: ").upper()

        if atv == "A":
            item = input("\nDigite o novo elemnto: ")
            if lista.count(item) == 0:
                adicionar(item)
                print(f"\n{item} adicionado com sucesso")
            else:
                print(f"\n{item} já está na lista")

        elif atv == "R":
            if len(lista) < 1 :
                print(f"\nNão há itens para ser removido")
            else:
                item = input("\nDigite o elemento que deseja apagar: ")
                if lista.count(item) >= 1:
                    remover(item)
                    print(f"\n{item} removido com sucesso")
                else:
                    print(f"\n{item} não encontrado na lista")

        elif atv == "L":
            mostra_lista()

        elif atv == "E":
           print(f"\nLista finalizada")
           mostra_lista()
           break

        else: 
            print("\nEntrada incorreta, preencha com as opções(A, R, L ou E) abaixo! ")

main()




