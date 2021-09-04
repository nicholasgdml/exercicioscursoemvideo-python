'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo'''
while True:
    print('-' * 35)
    print('Quer ver a tabuada de que número?')
    numero = int(input('> '))
    print('-' * 35)
    if numero < 0:
        break
    for c in range (1, 11):
        print(f'{numero} x {c} = {numero * c}')
print('Tabuada finalizada!! Volte sempre!!')