# Implemente um sistema que simule um carrinho de compras: adi¸c˜ao, remo¸c˜ao e
# total de itens com pre¸cos.
carrinho = []

itens_mercado = [
    {"nome": "Arroz", "preco": 15.50},
    {"nome": "Feijão", "preco": 6.30},
    {"nome": "Macarrão", "preco": 3.90},
    {"nome": "Óleo de soja", "preco": 7.50},
    {"nome": "Leite", "preco": 4.50},
    {"nome": "Pão", "preco": 7.00},
    {"nome": "Açúcar", "preco": 4.80},
    {"nome": "Café", "preco": 10.90},
    {"nome": "Sabonete", "preco": 2.50},
    {"nome": "Detergente", "preco": 3.10}
]

def menu():
    print("""
__________CARRINHO DE COMPRAS __________
          
A - ADICIONAR ITEM
R - REMOVER ITEM
T - TOTAL
E - SAIR

""")
    
def adicionar(cod, qnt):   
    dic = itens_mercado[(cod-1)]
    item = dic['nome']
    preco = dic['preco']
    carrinho.append((item, preco, qnt))
    return item

def remover(ide):
    item = carrinho[ide-1]
    carrinho.remove(item)
    return item

def calcular_total():
    print("""ID     ITEM      PREÇO     QNT.      TOTAL """)
    total = 0
    for i, item in enumerate(carrinho):
        valor = item[1] * item[2]
        total += valor
        print(f"""{i+1}     {item[0]}       {item[1]}       x{item[2]}       {valor}""")
    print(f"""\n                       VALOR DO CARRINHO:  {total}""")

def exibir_carrinho():
    print("""ID     ITEM      PREÇO     QNT.      TOTAL """)
    total = 0
    for i, item in enumerate(carrinho):
        valor = item[1] * item[2]
        total += valor
        print(f"""{i+1}     {item[0]}       {item[1]}       x{item[2]}       {valor}""")

def main():
    while True:
        menu()
        atv = input("Digite uma atividade: ").upper()

        if (atv == "A"):
            print("""
          
________ITENS________
COD.       ITEM        PREÇO
1    Arroz............ 15.50
2    Feijão............ 6.30
3    Macarrão.......... 3.90
4    Óleo de soja...... 7.50
5    Leite............. 4.50
6    Pão............... 7.00
7    Açúcar............ 4.80
8    Café............. 10.90
9    Sabonete.......... 2.50
10   Detergente........ 3.10

""")
            cod = int(input("Código do item: "))
            qnt = int(input("Quantidade: "))
            if cod > 0 and cod <= 10:
                item = adicionar(cod, qnt)
                print(f"{item} adicionado com sucesso!")
            else:
                print(f"{cod} não identificado nos itens disponíveis!")

        elif(atv == "R"):
            exibir_carrinho()
            ide = int(input("\nId: "))
            if ide > 0 and ide <= len(carrinho): 
                item = remover(ide)
                print(f"{item[0]} removido com sucesso!")
            else:
                print(f"{ide} não identificado no carrinho!")

        
        elif(atv == "T"):
            calcular_total()
        
        elif atv == "E":
           print(f"\nPrograma finalizado")
           break

        else:
            print("\nEntrada incorreta, preencha com as opções(A, R, T ou E) abaixo! ")

main()