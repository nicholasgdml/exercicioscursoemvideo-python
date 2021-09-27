def metade(num):
    valor = str(num / 2)
    return 'R$' + valor
    

def dobro(num):
    valor = str(num * 2)
    return 'R$' + valor


def aumentar(num, porcentagem=10):
    valor = str(num * (porcentagem/100))
    return 'R$' + valor


def diminuir(num, porcentagem=10):
    valor = num * (porcentagem/100)
    return 'R$' + valor
