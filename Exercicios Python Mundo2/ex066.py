contador = 0
soma = 0
while True:
    print('Digite um número (Digite 999 para parar):')
    numero = int(input('> '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A somas dos {contador} valores foram {soma}.')