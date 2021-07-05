# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
anonasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anonasc
print('Você tem {} anos.'.format(idade))
if idade <9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 19 and idade <=25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')   