'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e 
ímpares em ordem crescente.'''

num_list = list()
impares_list = list()
pares_list = list()

for c in range(0, 7):
    num_list.append(int(input('Digite um número: ')))

for num in num_list:
    if num % 2 == 0:
        pares_list.append(num)
    elif num % 2 == 1:
        impares_list.append(num)

print(f'Valores pares: {sorted(pares_list)}')
print(f'Valores impares: {sorted(impares_list)}')