# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
import datetime
from datetime import datetime
anoatual = datetime.now().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = anoatual - nascimento
ano1 = 18 - idade # Em quantos anos ira servir / Há quantos anos deveria ter servido.
ano2 = anoatual + ano1 # Ano de alistamento
print('Você nasceu em {} e tem {} anos em {}.'.format(nascimento, idade, anoatual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento!'.format(ano1))
    print('Seu alistamento será em {}'.format(ano2))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos!'.format(ano1 * -1))
    print('Seu alistamento foi em {}.'.format(ano2))
else:
    print('Você tem que se alistar IMEDIATEMENTE!')
