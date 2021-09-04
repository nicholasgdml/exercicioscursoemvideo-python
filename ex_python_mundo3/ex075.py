"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# Tupla
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais número: ')),
           int(input('Digite o último número: '))
           )

# Números selecionados
print(f'Os valores escolhidos foram {numeros}')

# A) Quantas vezes apareceu o valor 9.
if numeros.count(9) == 1:
    print(f'\nO número 9 apareceu 1 vez.')
else:
    print(f'O número 9 apareceu {numeros.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3.
print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição')

# C) Quais foram os números pares.
print(f'Os números pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')