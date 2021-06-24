import random
rn = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente divinhar...')
print('-=-'*20)
n = int(input('Que número eu pensei?: '))
if n == rn:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(rn, n))