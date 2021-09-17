"""Exercício Python 105: Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
- Situalçao (opcional)
"""


def notas(*num,sit=False):
    """-> Função para analisar notas e situações de varios alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional), indicando se deve ou não adicionar uma situação..
    :return: retorna um dicionario com várias informações sobre a situação da turma.
    """
    notas = dict()
    media = sum(num) / len(num)
    for n in num:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if sit:
        if media < 5:
            notas['situação'] = 'RUIM'
        elif 5 < media < 7:
            notas['situação'] = 'RAZOAVEL'
        else:
            notas['situação'] = 'BOA'
    notas['maior'] = maior
    notas['menor'] = menor 
    notas['média'] = media    
    return notas
        