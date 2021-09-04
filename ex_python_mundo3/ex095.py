'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogadores = list()
jogador = dict()
gols = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(0, partidas):
        gols.append(int(input(f' Quantos gols na partida {c+1}?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    r = str(input('Deseja continuar?[S/N]: '))[0]
    if r in 'Nn': break
print(jogadores)