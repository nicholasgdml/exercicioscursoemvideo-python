"""Exercício Python 107: Crie um módulo chamado moeda.py 
que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""

import moedas

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${moedas.metade(preco)}')
print(f'O dobro de R${preco} é R%{moedas.dobro(preco)}')
