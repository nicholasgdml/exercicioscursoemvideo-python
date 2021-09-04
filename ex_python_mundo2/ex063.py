'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''
print('-'*35)
print('Quantos termos você quer mostrar?')
t = int(input('> '))
c = 0
p = 0
a = 0
while c < t:
    print(p, end=' → ')
    p = p + a
    a = p - a
    c += 1
    if p == 0:
        p += 1
print('FIM')