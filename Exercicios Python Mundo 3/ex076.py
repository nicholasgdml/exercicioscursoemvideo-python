"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

# Tupla de produtos

produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.00,
            'Caneta', 22.30,
            'Livros', 34.90)

# Titulo

print('=' * 30)
print(f'{"Tabela de preços":^30}')
print('=' * 30)

# looping for que ultiliza impar e par para encontrar o preço e nome do produto

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:•<23}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')

# Linha para finalizar

print('=' * 30)
