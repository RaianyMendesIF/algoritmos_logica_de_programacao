
nome = input("\n Nome do funcionário: ")
quantidade_funcoes = int(input("\n Quantidade de funções criadas: "))
valor_funcao = int(input("\n Valor de cada função: "))

if quantidade_funcoes <= 0 or valor_funcao <= 0:
    print("Quantidade de funções e valor de função deve ser maior que zero!")
else:
    salario_bruto = quantidade_funcoes * valor_funcao
    desconto_inss = salario_bruto * 0.08
    salario_liquido = salario_bruto - desconto_inss

    print(f"""
    == SALÁRIO DE UM PROGRAMADOR ==
        
    Funcionário:     {nome}
    Salário Bruto:   {salario_bruto}
    Salário Líquido: {salario_liquido} 

    """)



