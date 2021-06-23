nome = str(input('Digite seu nome: ')).strip()
splitnome = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} \nSeu ultimo nome é {}'.format(splitnome[0], splitnome[-1]))