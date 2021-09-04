'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
print('Olá humano, sou seu computador...')
print('Pensei em um número de 0 a 10!')
print('Será que você consegue descobrir qual foi?')
computador = randint(0,10)
palpite = 0
tentativas = 0
while palpite != computador:
    palpite = int(input('Digite seu palpite: '))
    if palpite < computador:
        print('Mais... Tente novamente!')
    elif palpite > computador:
        print('Menos... Tente novamente!')
    tentativas += 1
print('Acertou com {} tentativas. PARABÉNS!!'.format(tentativas))