'''
LISTAS / TÚPLAS / DICIONÁRIOS

Listas -> Coleções heterogêneas de objetos, podem ser qualquer tipo, inclusive outras listas. 
- São mutáveis

[0, 10, "beto", [0.2, 0.3]]

n1, n2, n3 = 1, 2, 3 

lista01 = [3.14, 'beto', True,]
'''

lista = [1, 2, 3, 4, 5]
print(lista) 
#>>> [1, 2, 3, 4, 5]

print(lista[2])
#>>> 3

# len - função que retorna o tamanho de uma coleção
print(len(lista))
#>>> 5

#--------------------------------------------------#

lista = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']
# Formas de varrer uma lista

#1º 
for i in range(len(lista)):
    print(lista[i], end=' ')
#>>> 1 2 3 4 5

#2ª
for item in lista:
    print(item)
    
#Incluir novo elemento
lista.append('Guns')

#Trocar o último elemento
lista[-1] = "Novo elemento na última posição"

# Ordenar
lista.sort()

# Invertr a lista
lista.reverse()

#PESQUISA -> Pra que serve, como utilizar, quais são as restrições e casos de uso
# pop
# remove
# zip

for i, p in enumerate(lista):
    print(f'Posição {i}, Elemento: {p}')
# Função enumerate() retorna uma tupla de dois elementos a cada interação:
    
#--------------------------------------------------#

# Dada as seguintes listas [A, B, C] e [D, E, F] como poderíamos junta-las?
lista1 = ['A', 'B', 'C']
lista2 = ['D', 'E', 'F']

lista_completa = lista1 + lista2
print(lista_completa)
#>>> ['A', 'B', 'C', 'D', 'E', 'F']

"""
Pensando em listas de 50 alunos, onde serão lidas (random) 4 notas (0 - 100) mostre:
    a % de alunos aprovados
    a % de alunos reprovados
    
    imprima os 5 primeiros alunos com média mais alta
    imprime os 5 piores alunos
    imprima a nota mais alta, a posição qual aluno pertence 
    
""" 
# TUPLAS -> Semelhantes as listas, poém são imutáveis: não acrecentar, apagar, fazer atribuiçõs

tupla = (1, 2, 3, 4)

print(tupla[0])
#>>> 1

lista = list(tupla) #tuple

#PESQUISAS
# Set : o que ela tem em comun, é mutável, as restrições aplicação
# frozenset: Imutável ou não, desordenada 

#união, interseção e diferença 
# O que range ?