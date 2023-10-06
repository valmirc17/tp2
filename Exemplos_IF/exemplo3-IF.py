#Exemplo 3 - Comparativo de 3 números

numero1 = int(input("Digite o numero 1:"))
numero2 = int(input("Digite o numero 2:"))
numero3 = int(input("Digite o numero 3:"))
if numero1 == numero2 == numero3 :
    exit() #Encerra o programa

#Outra forma de IF ELSE é utilizar o ELIF
elif numero1 > numero2 and numero1 > numero3 :
    print("O primeiro número é o maior")
elif numero2 > numero1 and numero2 > numero3 :
    print("O segundo número é o maior")
elif numero3 > numero1 and numero3 > numero2 :
    print("O terceiro numero é o maior")