# Solicita o nome do corretor
nmCorretor = input("Digite o nome do corretor: ")
qtdImoveis = int(input("Digite a quantidade de imóveis vendidos: "))
vlTotal = float(input("Digite o valor total das vendas: R$ "))

salario_base = 1500.00
comissao_imovel = 200.00
comissao_valor_total = 0.05 * vlTotal
salario_final = salario_base + (comissao_imovel * qtdImoveis) + comissao_valor_total

print(f"O salário final de {nmCorretor} é de R$ {salario_final:.2f}")
