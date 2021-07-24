'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

contador = 0
contador1 = 0
precototal = 0
while True:
    contador1 += 1
    nomeproduto = str(input('Digite o nome do produto: ')).strip()
    precodoproduto = float(input('Digite o valor(ex:2.50): R$'))
    precototal += precodoproduto
    continuar = str(input('Deseja continuar? (S/N):')).upper().strip()[0]
    if precodoproduto > 1000:
        contador += 1
    if contador1 == 1:
        nomeprodutobarato = nomeproduto
        precoprodutobarato = precodoproduto
    elif precodoproduto < precoprodutobarato:
        nomeprodutobarato = nomeproduto
        precoprodutobarato = precodoproduto
    if continuar == 'N':
        break
print(f'O valor total da compra foi R${precototal:.2f}')
print(f'Você comprou {contador} produtos com valor maior que R$1000')
print(f'O produto mais barato foi {nomeprodutobarato} e custou R${precoprodutobarato}')