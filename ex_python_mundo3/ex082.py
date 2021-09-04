'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja continuar?[S/N]: ').upper().strip()[0]
    if r == 'N':
        break
for n in lista:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')