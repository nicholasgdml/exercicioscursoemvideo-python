"""Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""


def fatorial(numero, show=True):
    """-> Função retorna um número faturado!
        :param numero: Número a ser fatorado
        :param show: (opcional) Retorna a conta do fatorial (padrão True)
        :return: Retorna o número fatorado"""
    numeroFatorado = 1
    for c in range(numero, 0, -1):
        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                    print('1 =', end=' ')
        numeroFatorado *= c
    return numeroFatorado


print(fatorial(8))
print(fatorial(8, False))
