'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

dicionario = dict()
dicionario['nome'] = input('Nome: ')
dicionario['nota'] = float(input(f'Media de {dicionario["nome"]}: '))
if dicionario['nota'] > 7:
    dicionario['estado'] = 'Aprovado'
elif dicionario['nota'] > 6:
    dicionario['estado'] = 'Recuperação'
else:
    dicionario['estado'] = 'Reprovado'
print('-' * 30)
for k, v in dicionario.items():
    print(f'{k} é igual a {v}')