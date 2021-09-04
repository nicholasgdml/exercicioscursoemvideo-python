'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogadores = list()
jogador = dict()
gols = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(0, partidas):
        gols.append(int(input(f' -Quantos gols na partida {c+1}?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while True:
        r = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if r in 'SN': break
        else:
            print('Erro! Responda apenas com S ou N.')
    if r == 'N': break
print('='*37)
for k, v in enumerate(jogadores):
    if k == 0:
        print(f'{"cod":^3}', end='')
        for r in v.keys():
            print(f'{str(r):<15}', end='')    
        print()
        print('='*37)
    print(f'{k:^3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador?[999 para finalizar]?: '))
    if busca == 999:
        break
    elif busca >= len(jogadores):
        print('Comando Inválido! Tente Novamente!')
    else:
        print(f'    - Levantamento do jogador {jogadores[busca]["nome"]}')
        for k, v in enumerate(jogadores[busca]["gols"]):
            print(f'        No jogo {k+1} fez {v} gols')
        print('\n')
print('ENCERRANDO')
print('- VOLTE SEMPRE! -')