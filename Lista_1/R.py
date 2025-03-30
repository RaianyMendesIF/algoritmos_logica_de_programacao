print("===== CRÉDITO ESPECIAL =====")
saldo = float(input("Saldo médio no último ano: "))
mensagem = ""
valor_credito = 0.00

if saldo >= 0 and saldo <=200:
    valor_credito = 0.00
    mensagem = "Nenhum crédito disponível!"

elif saldo >= 201 and saldo <= 400:
    valor_credito = saldo * 0.2
    mensagem = "20% do valor do saldo médio"

elif saldo >= 401 and saldo <= 600:
    valor_credito = saldo * 0.3
    mensagem = "30% do valor do saldo médio"

elif saldo >= 601:
    valor_credito = saldo * 0.4
    mensagem = "40% do valor do saldo médio"

else:
    mensagem = "Nenhuma informação recebida"

print(f"Saldo médio: {saldo} \nPercentual: {mensagem} \nValor de crédito: {valor_credito}")


