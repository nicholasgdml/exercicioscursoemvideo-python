#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista em dinheiro/cheque')
print('[ 2 ] á vista no cartão')
print('[ 3 ] em 2x no cartão')
print('[ 4 ] em 3x ou mais no cartão')
opção = int(input('Selecione a forma de pagamento: '))
if opção == 1:
    novopreço = preço * 0.90
    print('Sua compra de R${} irá custar R${:.2f} no final'.format(preço, novopreço))
elif opção == 2:
    novopreço = preço * 0.95
    print('Sua compra de R${} irá custar R${:.2f}'.format(preço, novopreço))
elif opção == 3:
    parcela = preço / 2
    print('Sua compra será dividida em duas parcelas de R${}.\nTotalizando R${}'.format(parcela, preço))
elif opção == 4:
    nparcela = int(input('Digite a quantidade de parcelas: '))
    novopreço = preço * 1.20
    parcela = novopreço / nparcela
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(nparcela, parcela))
    print('Sua compra de R${} ira custar R${} no final'.format(preço, novopreço))
else:
    print('FUNÇÃO INVÁLIDA, TENTE NOVAMENTE!')