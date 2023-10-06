qtd_notas = int(input("Quantas notas você deseja inserir? "))
notas = []

for i in range(qtd_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

soma = sum(notas)
media = soma / qtd_notas

print(f"A média das {qtd_notas} notas é: {media:.2f}")
