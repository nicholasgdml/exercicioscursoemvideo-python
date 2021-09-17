"""Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
o programa se encerrará. Importante: use cores."""

def ajuda(x):
    help(x)


def menu(palavra):
    tam = len(palavra) + 4
    print('\033[1;30;107m')
    print('-' * tam)
    print(f'  {palavra}')
    print('-' * tam)
    print('\033[0m', end='')
    print()
    


while True:
    menu('Interactive Help')
    comando = str(input('Função ou Biblioteca > ')).strip().lower
    if comando in 'fim':
        break
    else:
        ajuda(comando)
menu('Fim!')