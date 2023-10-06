preco = 12.5
qtd_camisetas = int(input("Quantas camisetas você comprou? "))
total = qtd_camisetas * preco

if qtd_camisetas <= 5:
    desconto = 0.03
elif qtd_camisetas <= 10:
    desconto = 0.05
else:
    desconto = 0.07

valor_desconto = total * desconto
preco_final = total - valor_desconto

print(f"Preço total sem desconto: R${total:.2f}")
print(f"Desconto aplicado: {desconto * 100}%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Preço final com desconto: R${preco_final:.2f}")
