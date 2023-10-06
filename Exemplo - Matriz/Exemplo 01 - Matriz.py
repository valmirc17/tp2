# Exemplo 01 - Matriz

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Leitura de uma coluna específica

print('Mostre na primeira linha e primeira coluna', matriz[0][0])
print('Mostre na segunda linha e terceira coluna', matriz[1][2])
print('Mostre na terceira linha e segunda coluna', matriz[2][1])

print('Matriz')
for linha in matriz:
    print(linha)