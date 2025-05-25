# Dada uma lista de strings, crie uma nova lista com o tamanho (n´umero de caracteres) de cada string.
lista_string = ["Laranja", "Uva"]
lista_tam_string = []

for i in lista_string:
    lista_tam_string.append(len(i))

print(lista_tam_string)