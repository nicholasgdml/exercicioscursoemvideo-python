salario = int(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    print('Quem ganhava {} passa a ganhar {}'.format(salario, salario * 1.15))
else:
    print('Quem ganhava R${} passa a ganhar R${}'.format(salario, salario * 1.10))