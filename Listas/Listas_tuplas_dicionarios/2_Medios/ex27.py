# Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao
pilha = []

def menu(): 
    print("""
_______MENU_______

A - Adicionar item à pilha
R - Deletar item da pilha
E - Sair da pilha
""")
    
def adicionar(item):
    pilha.append(item)

def remover():
    pilha.pop()


def mostra_pilha():
    n = len(pilha)
    print("\n\n__________ITENS__________\n")
    for item in range(len(pilha)-1, -1, -1):
        print(f"{n} - {pilha[item]}")
        n -= 1
    print("\n_________________________\n\n")

def main():
    while True:
        menu()
        atv = input("Digite a atividade desejada: ").upper()
        if atv == "A":
            item = input("\nDigite o novo elemnto: ")
            adicionar(item)
            print(f"\n{item} adicionado com sucesso")
            mostra_pilha()
        elif atv == "R":
            if len(pilha) < 1 :
                print(f"\nNão há itens para ser removido")
            else:
                remover()
                print(f"\n{item} removido com sucesso")
            mostra_pilha()
        elif atv == "E":
           print(f"\nPilha finalizada")
           mostra_pilha()
           break
        else: 
            print("\nEntrada incorreta, preencha com as opções(A, R ou E) abaixo! ")

main()




