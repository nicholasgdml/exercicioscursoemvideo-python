'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                 
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja digitar outro número? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break
print(f'Foram digitados {len(lista)} termos.')
print(f'Os números de forma decrescente são {sorted(lista, reverse= True)}')
if lista.index(5) == 0:
    print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')