import random
nome1 = input('Digite o nome do Aluno 1: ')
nome2 = input('Digite o nome do Aluno 2: ')
nome3 = input('Digite o nome do Aluno 3: ')
nome4 = input('Digite o nome do Aluno 4: ')
nomes = nome1, nome2, nome3, nome4
aluno = random.choice(nomes)
print('O aluno escolhido foi {}'.format(aluno))