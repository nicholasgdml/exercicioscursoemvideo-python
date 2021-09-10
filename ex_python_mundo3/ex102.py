"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(numero, show=True):
    """Calcula o Fatorial de um numero
        :param numero: É o numero a ser Fatorado
        :param show: (opcional)  Mostra ou não a conta (Padrão True)
        :returm: O valor fatorado de numero"""

                
# Programa Principal
print(help(fatorial))
print(fatorial(8, False))
print(fatorial(10))