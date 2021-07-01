# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Olá')
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salario: R$ '))
tempo = int(input('Digite em quantos anos deseja pagar a casa: '))
parcela = valor / (tempo * 12)
parcelamaxima = salario * 0.30
print('Para uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor, tempo, parcela))
if parcela <= parcelamaxima:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO')
