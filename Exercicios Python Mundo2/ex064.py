'''Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
print('-'*40)
n1 = 0
n2 = 0
c = 0
while n1 != 999:
    print('Digite um número [999 para parar]')
    n1 = int(input('> '))
    if n1 != 999:
        n2 += n1
        c += 1
print('Você digitou {} números e a soma deles é {}'.format(c, n2))
print('-'*40)