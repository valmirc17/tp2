opcao=int(input("Qual grandeza deseja calcular? \n 1 - Tensão \n 2 - Resistência \n 3 - Corrente \n"))
if  opcao == 1 :
    resistencia=float(input("Informe a resistência:\n "))
    corrente=float(input("Informe a corrente:\n "))
    resultado = resistencia*corrente
    print(f"A tensão é de {resultado:.2f} Volts")
elif opcao == 2:
    tensao=float(input("Informe a tensão:\n "))
    corrente=float(input("Informe a corrente:\n "))
    resultado = tensao/corrente
    print(f"A resistência é de {resultado:.2f}Ohm")
elif opcao == 3:
    tensao=float(input("Informe a tensão:\n "))
    resistencia=float(input("Informe a resistência:\n "))
    resultado = tensao/resistencia
    print(f"A corrente é de {resultado:.2f}A")
else :
    print("Opção inválida!")
    exit()