'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
  sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
dados = {}
for c in range(0, 4):
    dados[f'jogador{c + 1}'] = randint(1, 6)
print(dados)