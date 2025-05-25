# Crie uma fun¸c˜ao que compare duas listas e retorne os elementos que est˜ao em ambas (interse¸c˜ao).

def gerar_intercecao(listaA,listaB):
    a = set(listaA)
    b = set(listaB)

    intersecao = list(a | b)
    return intersecao


lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print(gerar_intercecao(lista1,lista2))