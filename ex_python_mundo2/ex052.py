# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;31m', end='')
        t += 1
    else:
        print('\033[0;33m', end='')
    print(c, end=' ')
if t == 2:
    print('\033[m \n{} é um número PRIMO.'.format(n))
else:
    print('\033[m \n{} NÃO é um número PRIMO.'.format(n))