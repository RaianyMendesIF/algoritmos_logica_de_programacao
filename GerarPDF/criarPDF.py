from reportlab.pdfgen import canvas  # pip install reportlab
from reportlab.lib.pagesizes import A4 # A4 = (210*mm,297*mm)

#FUnção para converter mm em pontos
def mm2p(milimitros):
    return milimitros / 0.3527777



# Instância de um pdf
doc = canvas.Canvas("Ralatorio.pdf", pagesize=A4)

'''
# Permutar uma lista no pdf
nomes = ['caio', 'joão', 'marcos']
eixo = 287
for nome in nomes:
    doc.drawString(mm2p(10),mm2p(eixo), nome)
    eixo -= 5 # incrmento a posição para não ficarem em cima um do outro
'''
# ADICIONAR TEXTO - (Eixo X, Eixo Y, Texto)
doc.drawString(mm2p(10),mm2p(287), "Teste")

# ADICIONAR CÍRCULOS - (Eixo X, Eixo Y (X,Y do centro do cir.), Raio)
doc.circle(mm2p(105), mm2p(148), mm2p(20))

# ADICIONAR LINHA - (Xi, Yi, Xf, Yf)
doc.line(mm2p(10), mm2p(285),mm2p(200), mm2p(285))

# ADICIONAR UM RETÂNGULO (Yp1,Xp1,Yp3,Xp3)
doc.rect(200,250,300,350) #Quadrado

# ADICIONAR IMAGEM - (CAMINHO IMG, Ximg, Yimg, WIDTH=100, HEIGHT=200)
doc.drawImage("GerarPDF/codigos_pdf.png", 100, 250, width=100, height=80 )


doc.save()