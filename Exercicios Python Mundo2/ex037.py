# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
print('-'*34)
print('{:^34}'.format('ESCOLHA UMA FUNÇÃO!'))
print('-'*34)
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
print('-'*34)
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Função inválida\nFechando progama!')