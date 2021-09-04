# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Suas opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogada = int(input('Qual é sua escolha?: ')) - 1
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-'*30)
print('Computador jogou {}.'.format(itens[computador]))
print('Você jogou {}.'.format(itens[jogada]))
print('-'*30)
if computador == 0:
    if jogada == 0:
        print('EMPATE!!')
    elif jogada == 1:
        print('Jogador VENCEU!!')
    elif jogada == 2:
        print('Computador VENCEU!!')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 1:
    if jogada == 0:
        print('Computador VENCEU!!')
    elif jogada == 1:
        print('EMPATE!!')
    elif jogada == 2:
        print('Jogador VENCEU!!')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 2:
    if jogada == 0:
        print('Jogador VENCEU!!')
    if jogada == 1:
        print('Computador VENCEU!!')
    if jogada == 2:
        print('EMPATE!!')
    else:
        print('JOGADA INVÁLIDA!!')