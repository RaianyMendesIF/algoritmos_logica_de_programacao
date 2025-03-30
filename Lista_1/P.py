print("""
===== TRIÂNGULO =====
      
Digite os valores dos lados de um triângulo:""")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

soma_ab = a + b
soma_ac = a + c
soma_bc = b + c

a2 = a ** 2
b2 = b ** 2
c2 = c ** 2

if a < (b + c) and b < (a + c) and c < (a + b):

    if (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2):
        print("Triângulo Retângulo") 

    elif (a2 + b2 > c2) or (a2 + c2 > b2) or (b2 + c2 > a2):
        print("Triângulo Acutângulo")

    else:
        print("Triângulo Obtusângulo")
   
else:
    print("As medidas informadas não formam um triângulo!")





