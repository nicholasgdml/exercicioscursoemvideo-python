'''Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
continuar = 'S'
c = 0
numerototal = 0
numeromenor = 0
numeromaior = 0
while continuar == 'S':
    print('Digite um número:')
    numero = int(input('> '))
    print('Deseja continuar [S,N]')
    continuar = str(input('> ')).upper().strip()
    c += 1
    numerototal += numero
    if c == 1:
        numeromaior = numero
        numeromenor = numero
    elif numero > numeromaior:
        numeromaior = numero
    elif numero < numeromenor:
        numeromenor = numero
print('O menor número foi {}\n E o maoir foi {}'.format(numeromenor, numeromaior))
print('A média foi {}'.format(numerototal / c))