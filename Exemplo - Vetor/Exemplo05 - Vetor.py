# Exemplo Split

entrada = input('Digite os números do vetor separados por espaço: \n')
vetor = [int(x) for x in entrada.split()]

print('Vetor:', vetor)