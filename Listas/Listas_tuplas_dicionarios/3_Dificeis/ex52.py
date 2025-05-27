# Dada uma lista de strings, ordene por ordem do n´umero de vogais em cada string.

def contar_vogais(palavra):
    vogais = "AÃÁEÉÊIÍOÓÔÕUÚ"
    return sum(1 for letra in palavra if letra.upper() in vogais)

# Lista de strings
lista = ["python", "banana", "cachorro", "sol", "avião", "escola"]

# Ordenando pela quantidade de vogais (do menor para o maior)
lista_ordenada = sorted(lista, key=contar_vogais)

print(lista_ordenada)