numero = int(input("Informe um número inteiro positivo:"))

if numero % 2 == 0 :
    resultado = numero**2
    print(f"O quadrado do número informado é {resultado}.")
else :
    resultado = numero**3
    print(f"O cubo do número informado é {resultado}.")