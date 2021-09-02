'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, partidas):
    jogador['gols'] = [int(input(f' Quantos gols na partida {c}?: '))]
jogador['total'] = sum(jogador['gols'])
print('=' * 30)
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 30)
for k, v in enumerate(jogador['gols']):
    print(k, v)
