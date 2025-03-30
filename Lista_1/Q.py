w = float(input("Digite o valor de W: "))
z = float(input("Digite o valor de Z: "))

if (w > 0) or (z < 7):
    x = ((5 * w) + 1)/3
    t = ((5 * z) + 2)

else:
    x = ((5 * z) + 2)
    t = ((5 * w) + 1)/3

y = ((7 * x * 2) - (3 * x) - (8 * t)) / (5 * (x + 1))

print( f"Y = {y:.2f}")