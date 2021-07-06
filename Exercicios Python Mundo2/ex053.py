# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
frasei = frase[::-1]
print('O reverso de {} é {}'.format(frase, frasei))
if frase == frasei:
    print('Temos um PALÍNDROMO!!')
else:
    print('Não temos um PALÍNDROMO')
