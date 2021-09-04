# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
midade = 0 # Média de idade
idade20 = 0 # Idade menor que 20
idademaior = 0 # Maior idade
nomemaior = ''
for p in range (1, 5):
    print('{}ª pessoa'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    midade += idade
    if sexo == 'F':
        if idade < 20:
            idade20 += 1
    if sexo == 'M':
        if p == 1:
            idademaior = idade
            nomemaior = nome
        else:
            if idade > idademaior:
                idademaior = idade
                nomemaior = nome

print('A média da idade do grupo é {}'.format(midade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(idademaior, nomemaior))
if idade20 == 1:
    print('Ao todo se tem 1 mulher com menos de 20 anos')
else:
     print('Ao todo são {} mulheres com menos de 20 anos'.format(idade20))
