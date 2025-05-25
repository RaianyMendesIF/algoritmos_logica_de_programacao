# Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a ordem

nomes = ["Raiany", "Laís","Yasmin", "Yasmin", "Raiany", "Yasmin",  "Sara", "Raiany", "Laís", "Yasmin"]

print(nomes)

for i in nomes:
    qnt = nomes.count(i)
    if  qnt > 1:
        primeiro = nomes.index(i) + 1
        nova_lista = nomes[primeiro:]

        for j in range(qnt-1):
            nova_lista.remove(i)

        nomes = nomes[: primeiro] + nova_lista

print(nomes)
