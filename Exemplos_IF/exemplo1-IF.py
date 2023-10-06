#Estrutura de decisão
#Exemplo de cálculo de média ( 02 notas )

nota1 = int(input("Informe a nota do primeiro bimestre(0-10):"))
nota2 = int(input("Informe a nota do segundo bimestre(0-10):"))
media = (nota1 + nota2)/2

#Estrutura de decisão IF

if media >=6 :
    print("Aprovado!")
else :
    print("Reprovado!")