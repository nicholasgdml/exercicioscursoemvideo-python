import math
catoposto = float(input('Digite o cateto oposto: '))
catadja = float(input('Digite o cateto adjacente: '))
hip = math.hypot(catoposto, catadja)
print('A hipotenusa vai medir {:.2f}'.format(hip))