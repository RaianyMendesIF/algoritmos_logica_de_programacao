
def validar_opcao(maximo):
    while True:
        try:     # O bloco try é o código que pode causar um erro. 
            op = int(input("Opção: "))
            if 0 <= op <= maximo:
                return op
            else:
                print("Opção inválida, tente novamente!")

        except ValueError:  # Se houver um erro, o except informar sobre o problema no caso de argumento do tipo incorreto.
            print("Entrada inválida, digite um número.")