d = float(input('Qual é a distância da sua viagem(Km)?: ')) # d = Distancia do trejeto
p1 = d * 0.5 # p1 = Preço de viagem curta
p2 = d * 0.45 # p2 = Preço de viagem longa
if d < 200:
    print('Você está prestes a começar uma viagem de {} km'.format(d))
    print('E o preço da sua passagem será de R${}'.format(p1))
else:
    print('Você está prestes a começar uma viagem de {} km'.format(d))
    print('E o preço da sua passagem será de R${}'.format(p2))