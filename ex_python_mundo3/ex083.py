'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = input('Digite uma expressão: ')
parenteses = []
for p in exp:
    if p == '(':
        parenteses.append('(')
    elif p ==')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
if len(parenteses) == 0:
    print('Sua expressão está válida!!!')