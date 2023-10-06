nome = input("Informe o nome do corretor:")
qtd_imoveis = int(input("Informe a quantidade de imóveis vendidos:"))
vl_vendas = float(input("Informe o valor total das vendas"))
vl_salario_base = 1500
vl_salario_final = (200*qtd_imoveis)+(0.5*vl_vendas)+vl_salario_base
print(f"O salário final do corretor {nome} é de R${vl_salario_final}")