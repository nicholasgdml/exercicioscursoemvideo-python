'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    print('')
    print('{:=^30}'.format(' Qual opção deseja? '))
    print('  [ 1 ] somar')
    print('  [ 2 ] multiplicar')
    print('  [ 3 ] maior')
    print('  [ 4 ] novos números')
    print('  [ 5 ] sair do programa')
    print('=' * 30)
    opcao = int(input('>>>> Qual é sua opção? '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é', n1)
        else:
            print('O maior número é', n2)
    elif opcao == 4:
        print('Digite os novos números:' )
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Encerrando...')
    else:
        print('Opção invadida! Tente Novamente!')
    sleep(3)
print('Progama encerrado! Tenha um ótimo dia!')