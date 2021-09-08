"""Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep


def contador(x, y, z):
    cont = x
    print('~' * 30)
    print(f'Contagem de {x} até {y} de {z} em {z}')
    if y > x:
        while cont <= y:
            print(cont, end=' ')
            sleep(0.5)
            cont += z
    else:
        while cont >= y:
            print(cont, end=' ')
            sleep(1)
            cont -= z
    print()


contador(1, 10, 1)
contador(10, 0, 2)
x = int(input('Início: '))
y = int(input('Fim:    '))
z = int(input('Passos: '))
contador(x, y, z)
