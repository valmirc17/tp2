import random

vetor = [random.randint(0, 20) for _ in range(50)]

soma = 0
qtd_9 = 0
num_maior = vetor[0]

for valor in vetor:
    soma += valor
    if valor == 9:
        qtd_9 += 1
    if valor > num_maior:
        num_maior = valor

print("Vetor:", vetor)
print("Soma dos valores:", soma)
print("Número de ocorrências do valor 9:", qtd_9)
print("Maior valor no vetor:", num_maior)
