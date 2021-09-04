# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
# mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cadastro = list()
lista = list()
maior = menor = 0

while True:
    cadastro.append(input('Nome: '))
    cadastro.append(int(input('Peso[Kg]: ')))
    if len(lista) == 0:
        maior = cadastro[1]
        menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        elif cadastro[1] < menor:
            menor = cadastro[1]
    lista.append(cadastro[:])
    cadastro.clear()
    r = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if r == 'N': break

print(f'{len(lista)} pessoas foram cadastradas!!')
print(f'O maior peso foi {maior}Kg. Peso de', end=' ')
for item in lista:
    if item[1] == maior:
        print(f'{item[0]}', end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de',end=' ')
for item in lista:
    if item[1] == menor:
        print(f'{item[0]}', end='')