# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
    
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o número para a posição {c}: ')))
    if c == 0:
        menor_numero = lista[c]
        posicao_menor_numero = c
        maior_numero = lista[c]
        posicao_maior_numero = c
    else:
        if lista[c] < menor_numero:
            menor_numero = lista[c]
            posicao_menor_numero = c
        elif lista[c] > maior_numero:
            maior_numero = lista[c]
            posicao_maior_numero = c

print('-=-'*13)
print(lista)
print(f'O maior valor digitado foi {maior_numero} na posição {posicao_maior_numero}.')
print(f'O menor valor digitado foi {menor_numero} na posição {posicao_menor_numero}.')