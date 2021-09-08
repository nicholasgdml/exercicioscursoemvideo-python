'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                                                        
escreva(‘Olá, Mundo!’)
Saída:
~~~~~~~~~
Olá, Mundo!                                                                                                                                                          
~~~~~~~~~            
'''

def escreva(palavra):
    tamanhoPalavra = len(palavra)
    print('~' * (tamanhoPalavra + 4))
    print(f'    {palavra}')
    print('~' * (tamanhoPalavra + 4))

escreva('Nicholas')