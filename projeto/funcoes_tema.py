from dados.temas import temas, tipos_evento
from utilidades import validar_opcao, clear

def listar_temas():
    print("TEMA")
    for i,tema in enumerate(temas):
        print(f'{i+1} - {tema}')
    print("0 - Adicionar tema")

def adicionar_tema(novo_tema):
    temas.append(novo_tema)
    return len(temas)

#Ttpos de eventos
def listar_tipos_evento():
    print("TIPO DE EVENTO ")
    for i,tipo in enumerate(tipos_evento):
        print(f'{i+1} - {tipo}')
    print("")

def selecionar_tema():
    listar_temas()
    op = validar_opcao(len(temas))

    if op == 0:
        clear()
        novo_tema = input("NOVO TEMA: ")
        op = adicionar_tema(novo_tema)

    return temas[op-1]

# Adicionar um tema 
def adicionar_tema(novo_tema):
    temas.append(novo_tema)
    return len(temas)