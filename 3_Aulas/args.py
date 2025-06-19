#parâmetros obrigatórios, parâmetro opcionais

def parametro_obrigatorio(a):
    print(a) 
    
def parametro_opcional(a=5):
    print(a)
    
# isinstance   
# parametro_obrigatorio(7) #>>>7
# parametro_opcional(4) # >>>$
# parametro_opcional() # >>>5

# -----------------------------------------------------------------------------------------------

# *args : Convenções em Python que permitem que funções recebam um número variável de parâmetros
# Quando temos quantidades significativa de argumento utilizamos o args
def numero_sublistas_recursao(*args):      
    qnt_lista = 0 
    for item in args:
        if isinstance(item, list):
            qnt_lista += 1 + numero_sublistas_recursao(item)
            
    return qnt_lista 

from functools import reduce
def numero_sublistas_reduce(*args):
    return reduce(lambda count, item: count + (1 if isinstance(item, list) else 0), args, 0)


lista = 1,4,[5,6,3],[2, 6 ,2, 2, [4, 5, 6, 2]]    

# -----------------------------------------------------------------------------------------------

# GERAL

def soma(a, b, c):
    pass

#Parâmetros ordenado
soma(1, 2, 3)

#Parametros nomeados
soma(c = 2, a = 3, b = 4 )

#Lista de parâmetros nomeados
def funcao_completa(param_obg, *args, **kwargs):
    print(f'parâmetro obrigatório: {param_obg}')
    print(f'argumentos extras: {args}')
    print(f'Kwargs extras: {kwargs}')
    
#Exemplo de uso
funcao_completa("valor1", "extra1", "extra2", nome="Raiany", idade=18)



