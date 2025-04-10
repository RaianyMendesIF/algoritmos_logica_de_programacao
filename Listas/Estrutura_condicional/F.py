numeroA = int(input("Digite um número A: "))
numeroB = int(input("Digite um número B: "))

numero_aux = numeroA
numeroA = numeroB
numeroB = numero_aux

print(f"""
TROCA DE CONTEÚDOS
      
Número A : {numeroA}
Número B : {numeroB}
""")