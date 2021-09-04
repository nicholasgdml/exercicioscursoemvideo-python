# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range (1, 7):
    valor = int(input('Digite o {}º valor: '.format(c)))
    if valor %2 == 0:
        soma += valor
        cont += 1
print('A soma dos {} números pares foi {}'.format(cont, soma)) 