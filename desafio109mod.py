def dobro(n=0.0, formato=False):
    dob = n * 2
    return dob if formato is False else moeda(dob)

def metade(n=0.0, formato=False):
    metade = n / 2
    return metade if not formato else moeda(metade)

def diminuir(x=0, t=0, formato=False):
    dim = x - (x * t / 100)
    return dim if formato is False else moeda(dim)

def aumentar(x=0, t=0, formato=False):
    aumentar = x + (x * t / 100)
    return aumentar if formato is False else moeda(aumentar)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')