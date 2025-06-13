'''
RECURSIVIDADE
TÉCNICA DA APROGRAMAÇÃO ONDE UMA FUNÇÃO (chama a si mesma) PARA REOLVER ALGUM PROBLEMA

Principais características
1. Caso base: Condição de parada que evita chamadas infinitas
2. Caso recursivo: Onde a função 'chama a si mesma' com um problema menor


'''

def func(x):

    # Caso base
    if x < 1: 
        return 0 
    return x + func(x - 1)
    
'''
3 + func(2)
2 + func(2)
1 + func(0)
'''
    
# --------  print(func(10))

#FATORIAL DE 5

def fat(x):
    
    if x == 1:
        return 1
    
    return x * fat(x - 1)

print(fat(5))


# FIBONACCI (7) - > 1 1 2 3 5 8 13

def fib(x):
    if x <= 1: 
        return x
    return fib(x-1) + fib(x-2)

print(fib(7))

# Exe. 1 Inverter string: crie uma função recursiva que inverta uma string

def inverte(x):
    if len(x) == 0:
        return x
    
    return x[-1] + inverte(x[:-1]) # A posição zero mais a ultima letra do x sem a ultima 

print(inverte("raiany"))

# Exe. 2 Potência: Implemente uma função recursiva que calcule a^b, onde a e b são inteiros  b >= 0

def potencia(a, b):
    
    if b == 0:
        return 1
    
    return a * potencia(a, b-1)

print(potencia(3,2))