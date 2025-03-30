print("""
===== TRIÂNGULO =====
      
Digite os valores dos lados de um triângulo:""")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

soma_ab = a + b
soma_ac = a + c
soma_bc = b + c

if a < soma_bc and b < soma_ac and c < soma_ab:

    if a == b and b == c:
        triangulo = "equilátero"
    
    elif (a == b and b !=c) or (a == c and c != b ) or (b == c and c != a):
        triangulo = "isósceles"

    elif a != b and b != c and c != a:
        triangulo = "escaleno"

    print(f"O triângilo é {triangulo}!")
else:
    print("As medidas informadas não formam um triângulo!")
