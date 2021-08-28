'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.'''
soma = 0
soma_coluna = 0

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        soma += matriz[l][c]
        if c == 3: soma_coluna += matriz[l][c]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print('=' * 22)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 22)
print(f'A soma de todos os valores é {soma}.')
print(f'A soma de toddos os valores da terceira coluna é {soma_coluna}')
print(f'A maior valor da 2ª linha é {maior}')