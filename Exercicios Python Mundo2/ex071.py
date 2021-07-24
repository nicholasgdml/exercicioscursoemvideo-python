'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('-=-' * 10)
print('{:^30}'.format('Caixa Eletrônico'))
print('-=-' * 10)
valor = int(input('Digite o valor que deseja sacar: R$'))
total = valor
cedula = 50
totaldecedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totaldecedulas += 1
    else:
        if totaldecedulas > 0:
            print(f'{totaldecedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totaldecedulas = 0
        if total == 0:
            break