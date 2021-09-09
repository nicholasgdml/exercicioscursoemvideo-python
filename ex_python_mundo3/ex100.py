"""Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep

numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        randomNum = randint(0, 10)
        print(randomNum, end=' ')
        numeros.append(randomNum)
        sleep(0.5)
    print()


def somaPar(x):
    result = 0
    for n in x:
        if n % 2 == 0:
            result += n
    print(f'Somando os valores pares de {x}, temos {result}')


sorteia()
somaPar(numeros)