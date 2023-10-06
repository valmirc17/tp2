preco  = 12.50
qtd = int(input("Informe a quantidade de camisetas vendidas: "))
if qtd <= 5 :
    total = (preco*qtd)*0.97
elif qtd > 5 and qtd <= 10 :
    total = (preco*qtd)*0.95
elif qtd > 10 :
    total = (preco*qtd)*0.93
print(f"O valor final com o desconto é de: R${total:.2f}")