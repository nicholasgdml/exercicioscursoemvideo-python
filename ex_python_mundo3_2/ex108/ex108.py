"""Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor monetário formatado."""

import moedas1

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moedas.metade(preco)}')
print(f'O dobro de R${preco} é R${moedas.dobro(preco)}')
print(f'Aumentanto em 10% temos R${moedas.aumentar(preco)}')