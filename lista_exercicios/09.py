valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))

menor_valor = min(valor1, valor2, valor3)


soma = valor1 + valor2 + valor3 - menor_valor

print(f"A soma dos dois maiores valores é: {soma:.2f}")
