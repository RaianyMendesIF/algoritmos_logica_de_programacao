# 10. Dada uma lista de palavras, junte todas elas em uma string separada por v´ırgulas.

lista = [ "comida" , "uva", "roxo", "verde"]
frase = ""

for palavra in lista:
    frase += palavra + ", "
    
print(frase)