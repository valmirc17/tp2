preco = 1.99
print("Lojas Quase Dois - Tabela de preços")
for cont in range(1,51) :
    valor = cont*preco
    print (f"{cont} - R${valor}")