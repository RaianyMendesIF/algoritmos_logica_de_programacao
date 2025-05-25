# Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas com mais de 18 anos.
pessoas = [("Raiany", 19), ("Rian", 22), ("Kaique", 17), ("kauã", 10), ("Kauê", 3)]
maiores = []

for i in pessoas:
   if i[1]>= 18:
      maiores.append((i[0], i[1])) 

print("Maiores de idade: \n")
for i in maiores:
   print(f"{i[0]} - {i[1]} anos")