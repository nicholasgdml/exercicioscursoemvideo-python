import math
angulo = int(input('Digite o ângulo que você deseja: '))
Seno = math.sin(math.radians(angulo))
Cosseno = math.cos(math.radians(angulo))
Tangente = math.tan(math.radians(angulo))
print('O seno é igual a: {}'.format(Seno))
print('O cosseno é igual a: {}'.format(Cosseno))
print('A tangante é igual a:{}'.format(Tangente))