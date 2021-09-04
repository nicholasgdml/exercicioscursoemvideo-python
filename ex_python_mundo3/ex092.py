'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
anoAtual = datetime.now().year
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = anoAtual - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - anoAtual)
print('='*30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
