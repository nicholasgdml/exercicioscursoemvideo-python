from time import sleep
nome = str(input('Digite seu nome comepleto: ')).strip()
print('Analisando nome...')
sleep(3)
print('Seu nome em MAIÚSCULO é:{}'.format(nome.upper()))
print('Seu nome em MINÚSCULO é:{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))