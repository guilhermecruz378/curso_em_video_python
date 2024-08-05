lista = []
c = 0
while True:
    lista.append(int(input('Digite um número: ')))
    contin = input('Mais um? [S/N]').strip().upper()
    if contin[0] in 'Nn':
        break
'''impares = lista[:]
pares = lista[:]
print('Os números impares são: ',end=' ')
for c in range(0, len(impares)):
    if impares[c] % 2 != 0:
        print(impares[c],end=" - ")
print('Fim')
print('Os números pares são:',end=' ')
for c in range(0, len(pares)):
    if pares[c] % 2 == 0:
        print(pares[c],end=' - ')
print('Fim')'''
impares = list()
pares = list()
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print('=-='*15)
print(f'A lista de impares é: {impares}')
print(f'A lista de pares é: {pares}')