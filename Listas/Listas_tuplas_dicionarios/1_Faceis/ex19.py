#  Solicite nomes at´e que o usu´ ario digite ”sair”. Armazene em uma lista e imprima.
nomes = []
nome = ""

while nome != "sair":
    print("________ MENU ________ \na) Digite um nome para continuar; \nb) Ou 'sair' para finalizar a operação!")
    nome = input("R: ").lower()
    if nome != "sair":
        nomes.append(nome)
    
print(nomes)
    