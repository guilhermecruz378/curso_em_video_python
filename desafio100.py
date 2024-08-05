from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for cont in range(0, 5):
        #lista.append(randint(0,10))
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)


def somaPar(pares):
    print(f'Os valores pares são: ', end=' ')
    soma = 0
    for valor in pares:
        if valor % 2 == 0:
           sleep(0.3)
           print(valor, end=' ')
           soma += valor
    print('\nOs valores pares somados é igual à: ', end=' ')
    sleep(2)
    print(soma)
            


par = []
numeros = []
sorteio(numeros)
#print(numeros)
print()
somaPar(numeros)