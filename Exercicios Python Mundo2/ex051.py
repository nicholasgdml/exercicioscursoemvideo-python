# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('='*25)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print('='*25)
ptermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(ptermo, 11, razao):
    print(c,end=' → ')
print('Acabou')