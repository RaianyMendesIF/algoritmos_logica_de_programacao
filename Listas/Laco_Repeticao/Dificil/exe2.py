numero = int(input("Digite um número: "))
sequencia = [0, 1]
num_atual = 1
num_antecessor = 0
num_sucessor = 0


for i in range(numero-2):
    novo_numero = num_atual + num_antecessor

    sequencia.append(novo_numero)

    num_antecessor = num_atual
    num_atual = novo_numero

sequencia.reverse()

for i in sequencia:
    print(i, end=' ')

