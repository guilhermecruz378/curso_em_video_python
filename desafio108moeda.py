def dobro(n=0.0):
    dob = n * 2
    return dob

def metade(n=0.0):
    metade = n / 2
    return metade

def diminuir(x=0, t=0):
    dim = x - (x * t / 100)
    return dim

def aumentar(x=0, t=0):
    aumentar = x + (x * t / 100)
    return aumentar

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')