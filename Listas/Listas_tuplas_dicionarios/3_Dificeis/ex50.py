# Crie uma lista de tuplas com nomes e idades e retorne a pessoa mais velha e a mais nova

pessoas = [("Raiany", 18), ("Jociene", 47), ("Mario", 52)]
novo = ["", 0]
velho = ["", 0]

for i in pessoas:
    if i[1]> velho[1]:
        velho[0], velho[1] = i[0], i[1]

    if i[1] < novo[1] or novo[1] == 0 :
        novo[0], novo[1] = i[0], i[1]
        
print(f"{novo[0]} é o(a) mais novo(a) com {novo[1]} anos!")
print(f"{velho[0]} é o(a) mais velho(a) com {velho[1]} anos!")
