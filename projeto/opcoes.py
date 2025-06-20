from utilidades import validar_opcao, clear
from funcoes import cadastrar_evento, listar_eventos, editar_evento, buscar_evento, excluir_evento

def participantes_mais_ativos():
    contador = Counter()  

    # Passo 1: Percorrer cada evento da lista 'eventos'
    for evento in eventos:
        # Passo 2: Para cada participante inscrito no evento
        for pid in evento['participantes']:
            # Passo 3: Incrementa 1 na contagem desse participante (usando o ID dele)
            contador[pid] += 1

    # Passo 4: Seleciona os 3 participantes com maior número de participações
    mais_ativos = contador.most_common(3)

    # Passo 5: Exibe o resultado
    print("\n--- Participantes Mais Ativos ---")
    for pid, qtd in mais_ativos:
        nome = participantes[pid]['nome']  # Busca o nome do participante usando o ID
        print(f"{nome}: {qtd} eventos")

def Menu2(nome):
    clear()
    print(f'''
+----------------------------+
|      {    nome   }         |
+----------------------------+
| 1 - CADASTAR               |
| 2 - LISTAR                 |
| 3 - EDITAR                 |
| 4 - BUSCAR                 |    
| 5 - EXCLUIR                |
| 0 - VOLTAR                 |
+----------------------------+   ''')

def Eventos(): 
    while True:
        Menu2("   EVENTO   ")
        op = validar_opcao(5)
        clear()
        if op == 1:
            cadastrar_evento() 

        elif op == 2:
            listar_eventos()

        elif op == 3:
            editar_evento()

        elif op == 4:
            buscar_evento()

        elif op == 5:
            excluir_evento()
        
        elif op == 0:
            return


def Participantes():
    while True:
        Menu2("PARTICIPANTE")

        op = validar_opcao(5)
        clear()
        if op == 1:
            cadastrar_evento() 

        elif op == 2:
            listar_eventos()

        elif op == 3:
            editar_evento()

        elif op == 4:
            buscar_evento()

        elif op == 5:
            excluir_evento()
            
        elif op == 0:
            return
        




def Relatorios():
    while True:
        print(f'''
    +--------------------------------+
    |           RELATÓRIO            |
    +--------------------------------+
    | 1 - Eventos                    |
    | 2 - Usuários                   |
    | 3 - Participantes por evento   |
    | 4 - Participantes mais ativos  |
    | 5 - Temas mais frequentes      |
    | 0 - Voltar                     |
    +--------------------------------+   
                                    ''')
        op = validar_opcao(5)

        if op == 1:
            clear()
            

        elif op == 2:
            clear()
            
        
        elif op == 3:
            clear()
        

        elif op == 4:
            clear()
            
            
        
        elif op == 5:
            clear()

        elif op == 0:
            exit()
    