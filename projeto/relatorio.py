from utilidades import continuar, lista_vazia, titulo
from funcoes_evento import verificar_evento, listar_participantes
from dados.usuarios import usuarios
from dados.eventos import eventos

from collections import Counter #  contar a frequência de elementos em uma sequência
from reportlab.pdfgen import canvas  # pip install reportlab
from reportlab.lib.pagesizes import A4 # A4 = (210*mm,297*mm)


def listar_participantes_evento():
    titulo("PARTICIPANTES POR EVENTO")
    if lista_vazia(eventos):
        print("NÃO HÁ EVENTOS CADASTRADOS!")
    else:
        cod = int(input("CÓDIGO EVENTO: "))
        if verificar_evento(cod):
            print("EVENTO: ", eventos[cod]['nome'])
            listar_participantes(cod)
        else: 
            print("$# EVENTO NÃO IDENTIFICADO, VERIFIQUE O CÓDIGO E TENTE NOVAMENTE! $#")
    continuar()

def temas_frequentes():
    cont = Counter() # Contador vazio (como um dicionário)
    for cod in eventos:
            tema = eventos[cod]['tema']
            cont[tema] += 1 #Incrementa 1 na contagem do tema apartir do seu id
    frequentes = cont.most_common(10) # 10 temas que mais aparecem

    titulo("TEMAS FREQUENTES")
    if lista_vazia(frequentes):
        print("NÃO HÁ EVENTOS CADASTRADOS!")
    else:
        for tema, qnt in frequentes:
            print(f"{tema} - {qnt} eventos")
    continuar()

def participantes_mais_ativos():
    contador = Counter()  
    for cod in eventos:
        for matricula in eventos[cod]['participantes']:
            contador[matricula] += 1
    mais_ativos = contador.most_common(50)
    

    titulo("PARTICIPANTES MAIS ATIVOS")
    if lista_vazia(mais_ativos):
        print("NÃO HÁ PARTICIPANTES CADASTRADOS!")
    else:
        for matricula, qtd in mais_ativos:
            print(f"{usuarios[matricula]['nome']} - {qtd} eventos")

    continuar()
  

# EXPORTAR PDFs A4 = (210*mm,297*mm)

#Função para converter mm em pontos  
def mm2p(milimitros):
    return milimitros / 0.3527777


def exportar_lista_eventos(nome):
    try:
        doc = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        doc.drawString(mm2p(75),mm2p(y), "LISTA DE EVENTOS")
        y -= 10
 
        for key in eventos.keys():
            if y < 50:
                doc.showPage()
                y=287
            doc.drawString(mm2p(x1),mm2p(y), f"COD: {key}  |   EVENTO: {eventos[key]['tipo']} - {eventos[key]['nome']} ")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"TEMA: {eventos[key]['tema']}   |   MINISTRADOR: {eventos[key]['palestrante']}")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"DATA: {eventos[key]['data']}  |   HORA: {eventos[key]['hora']}   |   DURAÇÃO: {eventos[key]['duracao']} ")
            y -= 6
            doc.drawString(mm2p(x1),mm2p(y), f"LOCAL: {eventos[key]['local']}   |  PARTICIPANTES: {eventos[key]['qnt_participantes']}/{eventos[key]['max_participantes']}")
            y -= 6
            doc.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        doc.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")


def exportar_lista_usuarios(nome):
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE USUÁRIOS")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), "   ID   |                 NOME                  |               E-MAIL          |         QUANTIDADES DE EVENTOS        ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for key in usuarios.keys():
            if y < 25:
                use.showPage()
                y = 287
                use.drawString(mm2p(x1), mm2p(y), "   ID   |            NOME            |            E-MAIL          |        QUANTIDADES DE EVENTOS        ")
            use.drawString(mm2p(x1), mm2p(y), f"  {key} |   {usuarios[key]['nome']}   |   {usuarios[key]['email']}  |   {len(usuarios[key]['eventos'])}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")


def exportar_participante_evento(nome,cod):
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE PARTICIPANTES POR EVENTO")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f"EVENTO: {eventos[cod]['tipo']} - {eventos[cod]['nome']}  |  COD: {cod}")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for user in eventos[cod]['participantes']:
            if y < 25:
                use.showPage()
                y = 287
                use.drawString(mm2p(x1), mm2p(y), f"EVENTO: {eventos[cod]['tipo']} - {eventos[cod]['nome']}  |  COD: {cod}")
                y -= 3
                use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            use.drawString(mm2p(x1), mm2p(y), f"  {user}      {usuarios[user]['nome']}       {usuarios[user]['email']}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")


def exportar_participante_ativo(nome):
    cont = Counter()  
    for cod in eventos:
        for matricula in eventos[cod]['participantes']:
            cont[matricula] += 1
    mais_ativos = cont.most_common(50)
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE PARTICIPANTES MAIS ATIVOS")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f" ID    |            PARTICIPANTE                |         QUANTIDADE DE EVENTOS      ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for usua, qnt in mais_ativos:
            if y < 25:
                use.showPage()
                y = 287
            use.drawString(mm2p(x1), mm2p(y), f"{usua}      {usuarios[usua]['nome']}                 {qnt}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")


def exportar_temas_frequente(nome):
    cont = Counter() 
    for cod in eventos:
            tema = eventos[cod]['tema']
            cont[tema] += 1 
    frequentes = cont.most_common(10)
    try:
        use = canvas.Canvas(nome, pagesize=A4)
        x1 = 10
        x2 = 200
        y = 287 
        use.drawString(mm2p(75),mm2p(y), "LISTA DE TEMAS FREQUENTES")
        y -= 10
        use.drawString(mm2p(x1), mm2p(y), f"          TEMA                |         QUANTIDADE DE EVENTOS      ")
        y -= 3
        use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
        y -= 10
        for tema, qnt in frequentes:
            if y < 20:
                use.showPage()
                y = 287
            use.drawString(mm2p(x1), mm2p(y), f"{tema}                             {qnt}")
            y -= 6
            use.line(mm2p(x1), mm2p(y),mm2p(x2), mm2p(y))
            y -= 8
        
        use.save()
        print(f"DOCUMENTO EXPORTADO COM SUCESSO")
    except:
        print("#@ ERRO AO EXPORTAR O DOCUMENTO PDF! #@")


def verificar_usuarios():
    if len(usuarios) == 0:
        return False
    else:
        return True


def verificar_eventos():
    if len(eventos) == 0:
        return False
    else:
        return True