''' Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

print('='*30)
print('Gerador de PA')
print('='*30)
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
while c < 10:
    print('{}'.format(t), end=' → ')
    t += r
    c += 1
print('FIM')