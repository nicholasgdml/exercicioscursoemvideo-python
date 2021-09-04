'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

dados = dict()
pessoas = []
temp = 0
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('Erro!, Por favor digite M ou F.')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    dados.clear()
    while True:
        r = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print('Erro! Responda apenas com S ou N.')
    if r == 'N':
        break
print('-=-' * 10)
print(f'A) Temos {len(pessoas)} cadastradas.')
for dados in pessoas:
    temp += dados['idade']
media = temp / len(pessoas)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for dados in pessoas:
    if dados['sexo'] == 'F':
        print(dados['nome'], end= ' ')
print()
print('D) Lista das pessoas acima da média:')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print(f'    Nome = {pessoas[c]["nome"]}; Sexo = {pessoas[c]["sexo"]}; Idade = {pessoas[c]["idade"]}')
print('\n<ENCERRADO>') 
