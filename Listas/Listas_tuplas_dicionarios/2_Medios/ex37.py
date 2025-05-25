# Crie uma lista de palavras e remova as que tiverem menos de 4 letras.
palavras = ["Ovo", "Laranja", "Uva", "Imã", "Ilha", ]

for i in reversed(palavras):
    tam = len(i)
    if tam < 4:
        palavras.remove(i)

print(palavras)