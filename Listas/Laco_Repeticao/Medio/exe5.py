print(""" === MDC(Máximo Divisor Comum) ===""")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Não consegui utilizar o for

if num1 > num2:
    dividendo = num1
    divisor = num2
else:
    dividendo = num2
    divisor = num1

resto = dividendo % divisor


while resto != 0:
    dividendo = divisor
    divisor = resto
    resto = dividendo % divisor 

print(f"O MDC de {num1} e {num2} é {divisor}")