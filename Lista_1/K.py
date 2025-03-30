import math

print("""
===== EQUAÇÃO DO 2º GRAU =====
       aX^2 + bX + c = 0
      
Digite os respectivos valores:""")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = (b**2) - (4 * a * c)

if delta < 0:
    print("A função não possui raízes reais!")

elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    print(f"A expressão possui apenas uma raiz! \nraiz: {x1}")

elif delta > 0:
    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2*a)
    x2 = (-b - raiz_delta) / (2*a)
    print(f"\nraiz 1: {x1}\nraiz 2: {x2} ")

