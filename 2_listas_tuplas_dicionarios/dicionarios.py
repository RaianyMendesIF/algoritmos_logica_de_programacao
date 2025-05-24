'''
Dicionários 
Uma lista de associações compostas - Um objetos associado a outro objeto- por uma chave "única";

- Não vai haver um objeto com uma chave duplicada
- São mutáveis - os dados podem ser mutáveis mas as chaves não devem.
- Não fornece uma garantia de ordenação


lista = []
tupla =  , ,

"Eu preciso ter dois valores, o primeiro identifica a chave e depois o valor dessa chave"
"Qualquer elemento imutável pode ser uma chave!"


sintaxe: 
dicionario = {'Nome': 'Raiany', 'Idade': 18, 'Endereço': {'rua':38,'casa': 361, 'bairro':'Vila Piloto'}}


Estruturas 

'''

dic = {'nome1': 'Raiany', 'nome2': 'Sara','nome3': 'Yasmin', }

# Acessar conteúdo
dic['nome1'] # >>> Raiany

# Adicionar um conteúdo
dic['nota'] = 7.80 

#Usando print para debug
print(dic) # >> {'nome1': 'Raiany', 'nome2': 'Sara', 'nome3': 'Yasmin', 'nota': 7.8}

# for i in dic:
#     print(i,dic[i])

# Formas de operar sobre  os dicionários, Funções mais usuáis

#Armazenar os itens 
items = dic.items()

#Buscar todas as chaves
chaves = dic.keys()

#Buscar todas os valores
valores = dic.values()

#Buscar todas os valores



# As estruturas devem ser facilmente identificadas

print(f"Meus itens = {items}") # Retorna uma lista de tuplas
print(f"Meus keys = {chaves}")
print(f"Meus valores = {valores}")

# Operar volores dos itens do dic
for i, j in dic.items():
    print(f"i={i}, j = {j}")
    
    
# Operar volores de um dicionário
for i in dic.keys():
    print(f"i = {i}")
    
for j in dic.values():
    print(f"j = {j}")
    




