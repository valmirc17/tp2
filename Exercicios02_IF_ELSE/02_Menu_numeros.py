numero1 = int(input("Informe um número inteiro:"))
numero2 = int(input("Informe um outro número inteiro:"))
media_ponderada = ((numero1*2)+(numero2*3))/5
quadrado = (numero1+numero2)**2
if numero1 < numero2:
    menor=numero1**3
else:
    menor=numero2**3

opcao = int(input("Escolha uma opção: 1 - Média ponderada | 2 - Quadrado da soma dos dois números | 3 - Cubo do menor número: "))
if opcao == 1:
    print(f"A média ponderada é: {media_ponderada:.2f}")
elif opcao == 2:
    print(f"O quadrado da soma dos dois números é: {quadrado:.2f}")
elif opcao == 3:
    print(f"O cubo do menor número é: {menor}")
else:
    print("Opção inválida!")
    exit()