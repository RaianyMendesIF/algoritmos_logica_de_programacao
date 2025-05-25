# Inverta os elementos de uma lista sem usar o m´etodo reverse.

lista = ['Raiany', 'Vitoria', 'Prado', 'Mendes']
lista_inversa = []

for i in range(1,len(lista)+1):
    lista_inversa.append(lista[-i]) 

print(lista)
print(lista_inversa)