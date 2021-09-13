"""Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de
forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um
valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)"""


def leiaInt(pergunta):
    while True:
        num = str(input(pergunta))
        if num.isnumeric():
            num = int(num)
            return num
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[0;0m')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')