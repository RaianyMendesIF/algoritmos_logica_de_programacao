
eventos = {} 

temas = [
    'Desenvolvimento Web',
    'Inteligência Artificial', 
    'Segurança',  
    'Banco de Dados', 
    'Desenvolvimento Mobile', 
    'Redes de Computadores',  
    'Linguagens de Programação',
    'Análise de Dados', 
    'Ética e Privacidade',]

tipos_evento = [
    'Workshop',
    'Maratona de Programação', 
    'Palestra', 
    'Minicurso',]

def mostrar_temas():
    print("TEMA")
    for i,tema in enumerate(temas):
        print(f'{i+1} - {tema}')
    print("0 - Adicionar tema")


   

