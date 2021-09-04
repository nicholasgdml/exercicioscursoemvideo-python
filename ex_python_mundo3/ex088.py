'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import randint

lista = list()
temp = list()
quantiaListas = int(input('Quantos jogos você quer que eu sorteie?: '))

for j in range(0, quantiaListas):
    for n in range(0, 6):
        temp.append(randint(1, 60))
    lista.append(temp[:])
    temp.clear()
    
print(f'Sorteando {quantiaListas} jogos!')

for j in range(0, quantiaListas):
    print(f'Jogo {j + 1}: {lista[j]}')