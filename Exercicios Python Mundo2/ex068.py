'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint

print('-'*22)
print('Jogo do IMPAR ou PAR')
print('-'*22)
contador = 0
while True:
    print('Quantos dedos quer jogar?')
    ndedos = int(input('> '))
    print('Escolhe impar ou par? [i, p]')
    escolha = str(input('> ')).upper().strip()
    computador = randint(1, 10)
    total = ndedos + computador
    if escolha == 'P':
        print(f'Você jogou {ndedos} e o computador jogou {computador}')
        if total % 2 == 0:
            print(f'O total foi {total}, deu PAR')
            print('Jogadar Venceu!')
        else:
            print(f'O total foi {total}, deu IMPAR')
            print('Jogador Perdeu!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print(f'O total foi {total}, deu IMPAR')
            print('Jogador Venceu!')
        else:
            print(f'O total foi {total}, deu PAR')
            print('Jogador Perdeu!')
            break
    contador += 1
print(f'Fim do jogo! O jogador venceu {contador} vezes sequidas!')