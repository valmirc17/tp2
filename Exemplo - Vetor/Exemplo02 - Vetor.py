# Exemplo 02 - Vetor: -Definir tamanho do vetor(dinâmica)
#                     -Alocação de valores dentro do vetor

tamanho = int(input('Digite o tamanho do vetor:\n'))

vetor = []

# Estrutura de repetição
# O For executa de acordo com o tamanho digitado pelo usuário

for i in range (tamanho):
    
    # A variável elemento captura um número digitado para ser armazenado no vetor
    elemento = int(input(f'Digite o elemento {i + 1} do vetor: \n'))
    
    # Armazena o valor digitado (variável elemento) em uma posição no vetor
    vetor.append(elemento)

print('Vetor:',vetor)