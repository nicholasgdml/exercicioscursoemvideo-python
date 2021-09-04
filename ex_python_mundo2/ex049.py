# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite o número para ver sua tabuada: '))
for t in range(1, 11):
    tabuada = n * t
    print('{} x {:<2} = {}'.format(n, t, tabuada))

