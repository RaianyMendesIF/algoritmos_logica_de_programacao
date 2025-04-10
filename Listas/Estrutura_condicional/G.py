print("NOTAS BIMESTRAIS")

nota1 = int(input("1º nota: "))
nota2 = int(input("2º nota: "))
nota3 = int(input("3º nota: "))
nota4 = int(input("4º nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f"\n Estudante aprovado com media {media}")
else: 
    print(f"\nEstudante reprovado com media {media}")