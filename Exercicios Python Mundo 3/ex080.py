'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

lista = []
for c in range (5):
    num = int(input('Digite um número: '))
    for pos, valor in range(enumerate(lista)):
        if num < valor:
            lista.insert(pos, num)
            break
        else:
            lista.append(num)
print(lista)