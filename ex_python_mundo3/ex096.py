'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(a, b):
    area = a * b
    print(f'A área de um terro de {a} x {b} é de {area}m²!')



print('CONTROLE DE TERRENOS')
m1 = int(input('Largura[M]: '))
m2 = int(input('Comprimento[M]: '))    
area(m1, m2)
