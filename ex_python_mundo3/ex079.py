
'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

lista= []
while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Número repetido, digite novamente!')
    else:
        lista.append(n)
        r = input('Deseja continuar? [S,N]?: ').upper().strip()[0]
        if r == 'N':
            break
print(sorted(lista))