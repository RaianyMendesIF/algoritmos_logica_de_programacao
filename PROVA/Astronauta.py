passos = int(input("Qnts passos o astronauta deu? "))

pedras = 0
buracos = 0

for i in range(1, passos + 1):
    obs = input(f" Passo {i}, Pedra (P) ou Buraco (B)?").upper
    if obs == "P":
        pedras += 1
    elif obs == "B":
        buracos += 1
    else:
        print("Entrada inválida!")
        
print(f"Total de buracos encontrados: {buracos}\n ")
print(f"Total de pedras encontrados: {pedras}\n ")

if buracos > pedras:
    print("Cuidado mais buraco do que pedras!")