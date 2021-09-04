"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
  sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = []
for c in range(0, 4):
    dados[f'jogador{c+1}'] = randint(1, 6)
print('Valores sorteados:')
for i, v in dados.items():
    print(f'{i} tirou {v} no dado!')
    sleep(1)
print('-' * 26)
print(f'{"= Ranking de jogadores =":^26}')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
