from time import sleep
"""for c in range(0, 11):
        sleep(0.5)
        print(c,end=' ')
print()
print('-='*20)
for i in range(10, 0, -2):
        sleep(0.5)
        print(i, end=' ')
print()
print('-='*20)
def contador(x, y, z):
    print(f'Inicio -> {a} com o fim de -> {b} no passo... {c}')
    for z in range(a, b, c):
        sleep(0.5)
        print(z, end=' ')

print('AGORA É SUA VEZ DE REALIZAR A CONTAGEM')
a = int(input('inicio: '))
b = int(input('fim: '))
c = int(input('Passo: '))
print('-='*20)
contador(a, b, c)"""
#Resolução do professor

def linha():
    print('-='*20)

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*10)
    print(f' inicio de {i} com o final de {f} pulando de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += p
        print('FIM...')
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM...')


contador(0, 10, 1)
contador(10, 0, -1)
linha()
print('Agora é sua vez de personalizar a contagem...')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)