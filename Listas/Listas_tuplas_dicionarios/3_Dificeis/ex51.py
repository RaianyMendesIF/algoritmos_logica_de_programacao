# Implemente um sistema que funcione como fila de banco, com chegada e atendimento
# dos clientes.


fila = []

def chegada_cliente(nome):
    fila.append(nome)
    print(f"Cliente {nome} entrou na fila.")

def atender_cliente():
    if len(fila) > 0:
        cliente = fila[len(fila)-1] 
        fila.pop()
        print(f"Cliente {cliente} foi atendido.")
    else:
        print("A fila está vazia. Nenhum cliente para atender.")

def mostrar_fila():
    if len(fila) > 0:
        print(f"Fila atual: ")
        for i,pessoa in enumerate(fila):
            print(f"{i+1} - {pessoa}")
    else:
        print("A fila está vazia.")


chegada_cliente("Raiany")
chegada_cliente("Laís")
chegada_cliente("fabiany")

mostrar_fila()

atender_cliente()
atender_cliente()

mostrar_fila()

atender_cliente()
atender_cliente()