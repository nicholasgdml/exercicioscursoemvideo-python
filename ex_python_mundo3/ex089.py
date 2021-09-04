'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

notas = list()
temp = list()
while True:
    temp.append(input('Nome: '))
    for c in range(0, 2):
        temp.append(float(input(f'Nota {c+1}: ')))
    notas.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar?[s/n]: ')).strip()[0]
    if continuar in 'Nn':
        break
print('=' * 30)
print('-'*30)
print('Num', end=' ' * 4)
print('Nome',end=' ' *7 )
print('Media')
print('-'*30)
for p, n in enumerate(notas):
    print(f'{p}', end=' ' * 4)
    print(f'{n[0]:^10}', end=' ' * 4)
    print(f'{(n[1] + n[2]) / 2:2f}:')
while True:
    print('-' * 30)
    nota = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if nota == 999: break
    print(f'Notas de {notas[nota][0]} são {notas[1:]}')