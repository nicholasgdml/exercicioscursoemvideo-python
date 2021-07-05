# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes


s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos PODEM FORMAR um triângulo!')
    if s1 == s2 == s3:
        print('Este é um triângulo EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('Este é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo!')