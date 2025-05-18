# Algoritmos e lógica de Programação

Unidade curricular do curso superior Tecnólogo em Análise e Desenvolvimento de Sistemas / IFMS - CPTL

LINGUAGEM: Python

## Listas
> Lista 1 - 23/03/2025 (18 exercícios)
> Lista 2 - XX/XX/2025 (70 exercícios)


## Laço de repetição
Também chamados de loops, são comandos que permitem que comandos presentes no bloco sejam repetidos diversas vezes.
Necessário ter: Variável de controle, Condição de parada e Atribuição da variável de controle.

### For 
```
for i in range(2):
    print(i)
>>> 0, 1, 2
```

### While
```
while i <= 10:
    print(i, end=' ')
    i+= 1
>>> 1 2 3 4 5 6 7 8 9 10
```

## Listas
Coleções heterogêneas de objetos, podem ser qualquer tipo, inclusive outras listas.
```
lista = [1, 2, 3, 4, 5]
print(lista) 

# >>> [1, 2, 3, 4, 5]

for i in range(len(lista)):
    print(lista[i], end=' ')
# >>> 1 2 3 4 5

for item in lista:
    print(item)
```

### Incluir novo elemento
lista.append('Guns')

### Trocar o último elemento
lista[-1] = "Novo elemento na última posição"

### Ordenar
lista.sort()

### Invertr a lista
lista.reverse()

### Enumerate
```
for i, p in enumerate(lista):
    print(f'Posição {i}, Elemento: {p}')
```
> Função enumerate() retorna uma tupla de dois elementos a cada interação:

## PESQUISA -> Pra que serve, como utilizar, quais são as restrições e casos de uso

### pop
### remove
### zip
### Set : o que ela tem em comun, é mutável, as restrições aplicação
### frozenset: Imutável ou não, desordenada 
### união, interseção e diferença 
### O que range ?