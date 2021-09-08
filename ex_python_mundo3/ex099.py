"""Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar 
todos os valores e dizer qual deles é o maior."""

from time import sleep

def maior(*maior):
    print('~' * 30)
    print('Analisando os valores passados...')
    for k, v in enumerate(maior):
        print(v, end=' ')
        sleep(0.5)
        if k == 0:
            maior_valor = v
        else:
            if v > maior_valor:
                maior_valor = v
    print(f'Foram informados {len(maior)} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')


maior(10, 4)
maior(5, 11, 7, 10, 3, 9)
maior(1, 3, 1, 2)
maior(11, 1)
