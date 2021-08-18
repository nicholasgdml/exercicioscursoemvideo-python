"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('progamar', 'pao', 'joao', 'cafe', 'nicholas', 'computador')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')