real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.07
euro = real / 6.20
while True:
    print('-' * 50)
    print('Você quer converter seu dinheiro para?')
    print('1. Dolar')
    print('2. Euro')
    print('-' * 50)
    resposta = int(input('Resposta:'))
    if resposta == 1:
        print('Você tem {:.2f} dolares'.format(dolar))
        break
    elif resposta == 2:
        print('Você tem {:.2f} euros'.format(euro))
        break
    else:
        print('Numero errado, por favor digite novamente:')
        continue