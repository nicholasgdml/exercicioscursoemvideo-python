'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''
def linha():
    print('-'*100)

times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico-PR', 'Flamengo', 'Ceará', 'Atlético-GO', 'Bahia', 'Corinthians', 'Fluminense', 'Santos', 'Juventude', 'Internacional', 'Cuiabá', 'Sport', 'São Paulo', 'América-MG', 'Grêmio', 'Chapecoense')
linha()

# A
print('Os cinco primeiros times são:')
for c in range(0, 5):
    print(f'O {times[c]} que está na {c+1}ª posição!')
linha()

# B
print('Os 4 últimos times são:')
print(times[16:])
linha()

# C
print('Time em ordem alfabética:')
print(sorted(times))
linha()

# D
print(f'O Chapecoense está na posição {times.index("Chapecoense") + 1}ª posição! ')
linha()