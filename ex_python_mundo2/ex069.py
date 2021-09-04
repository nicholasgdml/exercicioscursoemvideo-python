'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
a = 0 # A) quantas pessoas tem mais de 18 anos.
b = 0 # B) quantos homens foram cadastrados.
c = 0 # C) quantas mulheres tem menos de 20 anos.

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()[0]
    print('-'*30)
    continuar = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]
    if continuar == 'N':
        break
    elif idade > 18:
        a += 1
    elif sexo == 'M':
        b += 1
    elif sexo == 'F':
        if idade < 20:
            c += 1
print(f'Temos {a} pessoas com mais de 18 anos.')
print(f'{b} homens foram cadastrados.')
print(f'Apenas {c} mulheres tem menos de 20 anos.')