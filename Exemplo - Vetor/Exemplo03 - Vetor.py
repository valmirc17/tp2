# Importando a biblioteca
import numpy as np

tamanho = int(input('Digite o tamanho do vetor:\n'))

# Definição do vetor através da biblioteca numpy
vetor = np.empty(tamanho, dtype=int)

for i in range(tamanho):
    elemento = int(input(f'Digite o elemento {i+1} do vetor: \n'))
    vetor[i] = elemento

print('Vetor:',vetor)
