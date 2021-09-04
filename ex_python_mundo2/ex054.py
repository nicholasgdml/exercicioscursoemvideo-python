# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
cont1 = 0 # variavel que conta menores de idade
cont2 = 0 # variavel que conta maiores de idade
for c in range(1, 8):
    ano = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        cont1 += 1
    elif idade >= 18:
        cont2 += 1 
print('Ao todo tivemos {} maiores de idade'.format(cont2))
print('e tivemos ao todo {} menores de idade'.format(cont1))