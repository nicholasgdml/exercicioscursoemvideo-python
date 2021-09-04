n = int(input('Digite um número: '))
print('Analisando o número {}...'.format(n))
u = n // 1 % 10     # Encontrar unidade com forma matematica 
d = n // 10 % 10    # Encontrar dezena com forma matematica
c = n // 100 % 10   # Encontrar centena com forma matematica
m = n // 1000 % 10  # Encontrar milhar com forma matematica
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))