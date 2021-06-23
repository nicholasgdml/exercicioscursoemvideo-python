dia = int(input('Por quantos dias o carro foi alugado?: '))
km = int(input('Quantos km rodado?: '))
aluguel = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${}!'.format(aluguel))