velocidade = int(input('Qual é a velocidade atual do carro: ')) # Declara uma variavel com a resposta da pergunta 'Qual é a velocidade atual do carro'
multa = (velocidade - 80) * 7.00
if velocidade > 80: 
    print('MULTADO! VocÊ excedeu o limite de velocidade que é de 80Km/h!')
    print('Você deve pagar uma mulda de R${:.2f}!'.format(multa))
print('Tenha um Bom Dia! Dirija com segurança!')