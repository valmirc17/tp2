linhas = int(input('Digite o número de linhas da matriz:\n'))
colunas = int(input('Digite o número de colunas da matriz:\n'))

# Não definido o tamanho da matriz

matriz_numeros = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        numero = float(input(f'Digite o número para a posição ({i},{j}):\n'))
        linha.append(numero)
    matriz_numeros.append(linha)
print (matriz_numeros)
# Exibição da matriz utilizando função join

for linha in matriz_numeros:
    print(' '.join(map(str,linha)))

# Função adicionar todo conteúdo dentro de uma string
# Map parâmetro da função join