#Exemplo com lista 1 - Break

localizar = "banana"
frutas = ["maçã","banana","laranja"]
for lista in frutas :
    if lista == localizar:
        print(f"Encontrado: {localizar}")
        break
    else:
        print(f"{localizar} não encontrado.")

#Exemplo com lista 2 - Continue

numero = [1,2,3,4,5,6,7,8,9,10]
for numero in numero :
    if numero % 2 == 0:
        #Pula os números pares
        continue
    print(f"Número impar: {numero}")

#Exemplo com lista criada pelo usuário

numeros_lista = []
for i in range(1,5) :
    numero = float(input(f"Digite o {i}º número:"))
    numeros_lista.append(numero)
    # O "append" serve para indicar que a lista receberá valores da variável

print("Números digitados:")
for numero in numeros_lista :
    print(numero)
    