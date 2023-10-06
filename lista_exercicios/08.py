renda_mensal = float(input("Informe a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Informe o valor total do empréstimo solicitado: R$ "))
numero_prestacoes = int(input("Informe o número de prestações desejadas: "))

valor_max_emprestimo = renda_mensal * 10

valor_max_prestacao = renda_mensal * 0.3

if valor_emprestimo <= valor_max_emprestimo and (valor_emprestimo / numero_prestacoes) <= valor_max_prestacao:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não pode ser concedido de acordo com os critérios estabelecidos.")
