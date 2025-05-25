# Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos num´ericos.



def soma_lista(lista):
    soma = sum(lista)
    return soma

lista = [25, 25, 25, 25, 100]

print("Soma dos elementos da lista: ", soma_lista(lista))